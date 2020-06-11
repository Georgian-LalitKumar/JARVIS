import speech_recognition as sr     #converts voice into text
import wikipedia    #module to extract information from wikipedia
import pyttsx3   # module used to convert text to speech
import sys
import datetime
import take_command
import webbrowser       #allows display of documents in webbrowser



#Provides application access to text-to-speech synthesis.
#The Speech Application Programming Interface or SAPI is an API developed by Microsoft
#  to allow the use of speech recognition and speech synthesis within Windows applications.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning Sir..!")
    elif hour>=12 and hour<18:
        speak("good afteernoon Sir..!")
    else:
        speak(" good evening Sir..!") 

    speak(" This is Jarvis AI . Your virtual assistant")
    speak("Initializing basic compatibility checkup")

def takeCommand():
    try:
        r= sr.Recognizer()
        with sr.Microphone() as source:
            speak(". Ready to accept command ")
            print("listening.....")
            r.pause_threshold = 1
            audio = r.adjust_for_ambient_noise(source,duration=1) # listen for 1 second to calibrate the energy threshold for ambient noise levels
            audio=r.listen(source)
    except Exception as e:
        speak("Sorry, We encountered an error . Please ensure Your Microphone is connected . ")
        speak("I have to terminate program . Thankyou")
        sys.exit()

    try:
        speak("processing Your Request . . please be  patient...")
        print("Processing Your Request. Please wait ...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")


    except Exception as e:

       #print(e)
        speak("say that again please....")
        return "None"
    return query



