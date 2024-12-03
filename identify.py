import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
import pygame

# Ensure the necessary directories exist
os.makedirs("persons", exist_ok=True)

def collect_data():
    name = input("Enter name of person: ")
    ids = input("Enter ID: ")

    count = 1
    cap = cv2.VideoCapture(0)

    # Load Haar Cascade for face detection
    cascade_path = "haarcascade_frontalface_default.xml"
    if not os.path.exists(cascade_path):
        print(f"Error: Haar Cascade file '{cascade_path}' not found.")
        return
    cascade = cv2.CascadeClassifier(cascade_path)

    while True:
        ret, frm = cap.read()
        if not ret:
            print("Error: Unable to access the camera.")
            break

        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.4, 1)

        for x, y, w, h in faces:
            cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = gray[y:y + h, x:x + w]
            cv2.imwrite(f"persons/{name}-{count}-{ids}.jpg", roi)
            count += 1
            cv2.putText(frm, f"Captured: {count}", (20, 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        cv2.imshow("Collect Data", frm)

        # Stop if 'Esc' is pressed or 300 images are captured
        if cv2.waitKey(1) == 27 or count > 300:
            print("Data collection completed.")
            cv2.destroyAllWindows()
            cap.release()
            train()
            break

def train():
    print("Training part initiated!")

    recog = cv2.face.LBPHFaceRecognizer_create()
    dataset = 'persons'
    paths = [os.path.join(dataset, im) for im in os.listdir(dataset) if im.endswith('.jpg')]

    faces = []
    ids = []

    for path in paths:
        try:
            ids.append(int(path.split('/')[-1].split('-')[2].split('.')[0]))
            faces.append(cv2.imread(path, 0))
        except Exception as e:
            print(f"Error processing file {path}: {e}")

    if len(faces) == 0:
        print("No data to train on.")
        return

    recog.train(faces, np.array(ids))
    recog.save('model.yml')
    print("Training completed.")

def identify():
    cap = cv2.VideoCapture(0)

    # Initialize pygame mixer for sound playback
    pygame.mixer.init()
    pygame.mixer.music.load("buzz.wav")

    cascade_path = "haarcascade_frontalface_default.xml"
    if not os.path.exists(cascade_path):
        print(f"Error: Haar Cascade file '{cascade_path}' not found.")
        return
    cascade = cv2.CascadeClassifier(cascade_path)

    # Load trained model
    if not os.path.exists('model.yml'):
        print("Error: Trained model 'model.yml' not found.")
        return
    recog = cv2.face.LBPHFaceRecognizer_create()
    recog.read('model.yml')

    paths = [os.path.join("persons", im) for im in os.listdir("persons") if im.endswith('.jpg')]
    labelslist = {path.split('/')[-1].split('-')[2].split('.')[0]: path.split('/')[-1].split('-')[0] for path in paths}
    print("Loaded labels:", labelslist)

    while True:
        ret, frm = cap.read()
        if not ret:
            print("Error: Unable to access the camera.")
            break

        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 2)

        for x, y, w, h in faces:
            cv2.rectangle(frm, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi = gray[y:y + h, x:x + w]

            try:
                label = recog.predict(roi)
                if label[1] < 100:
                    cv2.putText(frm, f"{labelslist.get(str(label[0]), 'Unknown')} ({int(label[1])})", 
                                (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(frm, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    if not pygame.mixer.music.get_busy():  # Play alert if not already playing
                        pygame.mixer.music.play()
            except Exception as e:
                print(f"Error during prediction: {e}")

        cv2.imshow("Identify", frm)

        if cv2.waitKey(1) == 27:
            print("Exiting identification.")
            cv2.destroyAllWindows()
            cap.release()
            break

def maincall():
    root = tk.Tk()
    root.geometry("480x200")
    root.title("Face Identification System")

    label = tk.Label(root, text="Select below buttons")
    label.grid(row=0, columnspan=2)
    label_font = font.Font(size=20, weight='bold', family='Helvetica')
    label['font'] = label_font

    btn_font = font.Font(size=15)

    button1 = tk.Button(root, text="Add Member", command=collect_data, height=2, width=20)
    button1.grid(row=1, column=0, pady=(10, 10), padx=(5, 5))
    button1['font'] = btn_font

    button2 = tk.Button(root, text="Start with Known", command=identify, height=2, width=20)
    button2.grid(row=1, column=1, pady=(10, 10), padx=(5, 5))
    button2['font'] = btn_font

    root.mainloop()

# Start the application
maincall()
