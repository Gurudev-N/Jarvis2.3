import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime #pip install datetime
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import os #pip install os
import smtplib #pip install smtplib
from pprint import pprint #pip install smtplib
import discord #pip install discord
import Calculator #pip install calculator
import subprocess as sp
import pywhatkit as kit
import pyautogui
import tkinter

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir...!")
        print("Good Afternoon sir...!")   

    else:
        speak("Good Evening sir...!")
        print("Good Evening sir...!")  

    speak("I am Jarvis sir!.How may I help you")
    print("I am Jarvis sir!.How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak("okay sir..I am on it!")

    except Exception as e:
        # print(e)    
        print("Please say that again please...") 
        speak("Please say that again please...")   
        return "None"
    return query

def play_on_youtube(video):
    kit.playonyt(video)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            youtubePath='C:\\Users\Sony Joseph\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\YouTube.lnk'
            print("opening")
            os.startfile(youtubePath)

        elif 'open google' in query:
            googlePath='C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
            print("opening")
            os.startfile(googlePath)

        elif 'open whatsapp' in query:
            print("opening")
            webbrowser.open("web.whatsapp.com")

           

        elif 'open discord' in query:
            discordPath = "C:\\Users\Sony Joseph\AppData\Local\Discord\Discord.lnk"
            print("opening")
            os.startfile(discordPath)

        elif 'open studio' in query:
            studiocodePath = "C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019.lnk"
            print("opening")
            os.startfile(studiocodePath)

        elif 'play music' in query:
            music_dir = 'C:\\Users\Sony Joseph\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            print("opening")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\Sony Joseph\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            print("opening")
            os.startfile(codePath)

        elif 'email to rohan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rohansony855@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")   

        elif 'jarvis quit' in query:
            print("jarvis:Quitting sir!..Thanks for your time sir")
            speak("Quitting sir!..Thanks for your time sir")
            quit()
        
        elif 'open cmd' in query:
            cmdPath = "C:\\WINDOWS\system32\cmd.exe"
            print("opening")
            os.startfile(cmdPath)

        elif 'close youtube' in query:
            youtubePath='C:\\Users\Sony Joseph\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\YouTube.lnk'
            print("closing")
            os.close()

        elif 'close google' in query:
            googlePath='C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
            print("closing")
            os.close()


        elif 'close whatsapp' in query:
            print("closing")
            webbrowser.close()

        elif 'close discord' in query:
            discordPath = "C:\\Users\Sony Joseph\AppData\Local\Discord\Discord.lnk"
            print("closing")
            os.close()


        elif 'close studio' in query:
            studiocodePath = "C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio 2019.lnk"
            print("closing")
            os.close()

        elif 'close code' in query:
            codePath = "C:\\Users\Sony Joseph\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            print("closing")
            os.close()
   
        elif 'open cmd' in query:
            cmdPath = "C:\\WINDOWS\system32\cmd.exe"
            print("closing")
            os.close()