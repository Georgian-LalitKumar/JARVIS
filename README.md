# JARVIS
I have develop a small AI System which takes Voice Commands from the user via microphone and convert into text commands which is then used to automate the system accordingly. 
You can take a look on youtube for Demo:https://www.youtube.com/watch?v=nnklGb0kqkA&feature=youtu.be

-->>MAIN.py 
   This file initiates the Voice Command mode.
   It imports some user-defined module like speak_receive and take_command.

-->>speak_receive.py
  In this file speak function, wishMe function and takeCommand function has been defined.
  -speak function: is used to convert provided input text to audio.
                    e.g: speak("Wow, What a Great Day!").
  -wishMe function: it wish the according to the time in your system.
  -takeCommand function : is used to take input from the user via microphone and convert it
                          into text for further processing of queries.                          
  This file imports speechRecognition, pyttsx3, wikipedia, sys, datetime, webbrowser and take_command modules.
      - speechRecognition: This mnodue is used to converts voice data into text data.
      - pyttsx3: This module is responsible to convert text back to speech (which is useful for audio interaction).
      - wikipedia: This module is responsible to extract information from wikipedia.
      - datetime: This module is used to take date and time from the System(on which it is running).
      - sys: This module provides access to some variables used or maintained by the interpreter and
              to functions that interact strongly with the interpreter.  
      - webbrowser: This module allows display of documents or search of query in webbrowser.
      
-->>take_command.py
  This file is responsible for taking return query from  speak_receive.py file and process the query.
  Basically it searches for a specific command in the returned query , and processes accordingly.
  This programme is capable of doing following things:
    -Searching on YouTube.
    -Searching on Google.
    -Opening different websites.
    -Extracting information from Wikipedia.
    -Playing music (audio and video ) from local disk.
    -Sending Mail.
    -Taking screenshot.
  This file also contains Pillow module, which is used here to take a screenshot, when given command. 
  
-->>Gesture Recognition And Virtual Mouse Controlling
  It contains detector.py, trainer.py, gesture_working.py and gesture_control_monitor.py
  -detector.py: This file is used to create a dataset of images for trainer.py and gesture_working.py
                and the data is saved in dataSet folder.
               --It containes cv2 and numpy modules.
                 -cv2(OpenCV): OpenCV-Python is a library of Python bindings designed to solve
                              computer vision problems.OpenCV-Python makes use of Numpy.
                 -numpy:OpenCV-Python makes use of Numpy, which is a highly optimized library 
                        for numerical operations with a MATLAB-style syntax.
                        All the OpenCV array structures are converted to and from Numpy arrays.
                        This also makes it easier to integrate with other libraries that use 
                        Numpy such as SciPy and Matplotlib.

  -trainer.py: This file is used to train the dataSet which was collected via detector.py and produces a 
               trainingData.yml file in recognizer folder which is used for face recognition.
  
  -gesture_working: This file uses the trained model i.e trainingData.yml for recognizing the faces.
                    It takes input from the web camera and tries to recognize the face or object.
    
  -gesture_control_monitor: This file is used to recognize hand movements(green color) and control mouse according 
                            to hand movements.
      -The following modules are important to install to make the face Recognition working.
      -pynput:This library allows you to control and monitor input devices. 
              Currently, mouse and keyboard input and monitoring are supported. 
      -wxpython:DescriptionwxPython is a wrapper for the cross-platform GUI API wxWidgets for the
                Python programming language. It is one of the alternatives to Tkinter. 
  
  


  
      
