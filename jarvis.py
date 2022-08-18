from ast import Try
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour > 0 and hour < 12):
        speak("Good Morning!")
    elif(hour >=12 and hour < 18):
         speak("Good Afternoon!")
    else:
         speak("Good Evening!")
    
    speak("I am Jarvis Sir. Please tell me how may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("lcs2019013@iiitl.ac.in",'password-likhna hai')
    server.sendmail('lcs2019013@iiitl.ac.in',to,content)
    server.close()



def takeCommand():
    # It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognition...')
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Pardon me, Say that again Please...")
        return "None"
    return query

if __name__ == "__main__":
    if 1: 
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            speak('Opening youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            speak('Opening stack over flow...')
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            code_path = "C:\\Users\\Mobbshir Perwez\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'mail to mobasshir' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "perwezmobasshir@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("ERROR FOUND IN SENDING EMAIL.")
