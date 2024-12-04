1.  Install Required Libraries 
    • Before running the program, make sure you have the necessary 
      libraries installed. You can install them using pip. 
    • OpenCV: For video processing and motion detection. 
      (pip install opencv-python) 
    • Pygame: For playing sound when motion is detected. 
      (pip install pygame) 


2.  Prepare Your File 
    • Create the Directory 
    • Organize Directories for Storing Images: 
       (i) motion_captures: To store images captured when motion 
           is detected. 
       (ii) visitors/in: To store images of visitors entering 
       (iii) visitors/out: To store images of visitors exiting.  


3.  Add Sound File for Alert 
    • Make sure you have a sound file (e.g., buzz.wav) to alert when 
      motion is detected. Place the sound file in the same directory as the 
      program or adjust the path in the code accordingly. 


4.  Run The Code 
    • Open a Terminal or Command Prompt: Navigate to the folder 
      where your Python script is located. 
    • Run the Python script by executing the following command: 
      (python your_script_name.py) 
    • For example, if your file is named visitor_detection.py, the 
      command will be: 
      (python visitor_detection.py) 


5.  Interact With Program 
    It opens the Interface. 
      (i) Zone Alert: 
          • Right-click to define the specific zone of the region. 
          • It stores the motion detection zone in file with current date and time. 
      (ii) Snap Guard: 
           • The spot_diff () function is called to detect differences between two 
             consecutive frames. 
           • To get any object from frame that it gets alert and stores in the file. 
      (iii) Visitors Detection: 
            • If the motion is detected in the right region (e.g., visitors entering or 
              exiting), the program will capture the image of the visitor and save it 
              the visitors/in or visitors/out folders, depending on the direction of motion. 
      (iv) Identification: 
           • First add the member and create identity of a person. 
           • Next give start with known and it identifies them by matching their 
             image with the stored profile. 
      (v)  Record: 
           • It monitors the covered area with current date and time, then it stores 
             the recordings in the file.  
      (vi) Lock Frame: 
           • It is similar to the Zone Alert but it capture’s the whole covered area 
             and detect the objects. 

6.  Existing The Program: 
    To stop the program, simply press the Esc key or click Exit button in the interface.
