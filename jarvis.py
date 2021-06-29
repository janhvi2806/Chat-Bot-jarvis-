import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak('Good Evening!')

    speak("I am Python .please tell me how may i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Hearing.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        queryy=r.recognize_google(audio,language="en-in")
        print(f"User said:- {query}\n")
    
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return queryy

def sendEmail(to,content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gamilc.om','Your-password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
    #takeCommand()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("Wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        
        elif 'open code' in query:
            codePath= "" #visual path
            os.startfile(codePath)

        elif 'email to person' in query:
            try:
                speak('What should i say')
                content =  takeCommand()
                to ="person@gmailcom"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry i can't do that rn")

        elif 'play music' in query:
            music_dir = "File location please"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'open whatsapp' in query:
            webbrowser.open("whatsappweb.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open teams' in query:
            codePaths= "" #visual path
            os.startfile(codePaths)
        
        elif 'open meet' in query:
            webbrowser.open('meet.google.com')

        elif 'open github' in query:
            webbrowser.open('github.com')

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open coursera' in query:
            webbrowser.open("coursera.com")
        
        elif 'open udemy' in  query:
            webbrowser.open("udemy.com")
        
        elif 'vit bhopal' in query:
            webbrowser.open("vitbhopal.ac.in")
