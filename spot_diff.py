import cv2
import time
from skimage.metrics import structural_similarity
from datetime import datetime
import beepy


def spot_diff(frame1, frame2):
    # Ensure frames are valid
    if frame1 is None or frame2 is None:
        print("Error: One or both frames are None.")
        return 0

    frame1 = frame1[1]
    frame2 = frame2[1]

    if frame1 is None or frame2 is None:
        print("Error: Failed to process the frames correctly.")
        return 0

    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    g1 = cv2.blur(g1, (2, 2))
    g2 = cv2.blur(g2, (2, 2))

    (score, diff) = structural_similarity(g2, g1, full=True)
    print("Image similarity:", score)

    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY_INV)[1]

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = [c for c in contours if cv2.contourArea(c) > 50]

    if len(contours):
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the images in non-blocking mode
        cv2.imshow("Difference", thresh)
        cv2.imshow("Detected Objects", frame1)

        # Save the frame with the bounding boxes
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        cv2.imwrite(f"stolen/{timestamp}.jpg", frame1)

        # Play a sound alert
        beepy.beep(sound=10)

    else:
        print("Nothing stolen")
        return 0

    # Keep the windows responsive
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to close the windows
            break

    cv2.destroyAllWindows()
    return 1

# Test the function
if __name__ == "__main__":
    # Capture video feed
    cap = cv2.VideoCapture(0)  # Use the default camera

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        exit()

    print("Capturing frames for testing...")

    ret1, frame1 = cap.read()
    time.sleep(2)  # Allow time for motion or changes
    ret2, frame2 = cap.read()

    if not ret1 or not ret2:
        print("Error: Could not read frames from the camera.")
        cap.release()
        exit()

    # Call the function
    spot_diff((ret1, frame1), (ret2, frame2))

    # Release the video capture
    cap.release()
