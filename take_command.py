import speak_receive
import datetime  #used to get current date and time
import webbrowser       #allows display of documents in webbrowser
import os               #allows to use operating system dependent functionalities
import smtplib          #allows to work with emails and email server
import re        #used for string searching and manipulation. & extract large amount of data from websites
from PIL import ImageGrab       #allows to take a snapshot of a screen
import speech_recognition as sr     #converts voice into text
import wikipedia    #module to extract information from wikipedia
import pyttsx3   # module used to convert text to speech
import sys

def queries(query):
    if True:
        #if 1:
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak_receive.speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak_receive.speak("According to wikipedia")
            speak_receive.speak(results)
            

        #opening youtube
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        
        
        
            # to search via command on google
        elif ' on google'in query:
            try:

                from googlesearch import search 
            except ImportError: 
                print("No module named 'google' found")       
            for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
                webbrowser.open(j) 

            #opening stackoverflow website
        elif 'open stackoverflow'in query:
            webbrowser.open("stackoverflow.com")
            
            
            
            # to play music on local device
        elif 'play music' in query:
            music_dir ='E:\\audios'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
            
            
            # to get the time update
        elif ' time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_receive.speak(f"sir, the time is {strTime}")

        elif 'open code ' in query:
            codePath="C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
            
            
            # to kill the terminal
        elif 'close ' in query:
            speak_receive.speak("terminating session Sir . Have a nice day sir ")
            sys.exit()
                
            
            # to send an email via voice
        elif 'send email' in query:
            try:
                speak_receive.speak("what should i say ?")
                content = takeCommand()
                to =""
                sendEmail(to,content)
                speak_receive.speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak_receive.speak("sorry email has not been sent ,sir!")
            
            
            # to take a screenshot via voice command
        elif 'screenshot' in query:
            img=ImageGrab.grab()
            img.save('C://screenshot.bmp')
            speak_receive.speak(f"this is screenshot captured")
            img.show()
            
            
            # to search on youtube via command  
        elif 'on youtube' in query:
            webbrowser.open("https://www.youtube.com/results?search_query=" + str(query))

        