import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        # r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please.....")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hello")
    speak("I am Jarvis Ma'am. Please tell me how may i help you")

wishMe()
while True:
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google chrome' in query:
        chromePath = ("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        os.startfile(chromePath)
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")

    elif 'open spotify' in query:
        spotifyPath = ("C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe")
        os.startfile(spotifyPath)


