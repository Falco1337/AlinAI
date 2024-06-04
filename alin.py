import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import wikipedia


os.system("clear")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
engine.setProperty("voice", voices[11].id)

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        os.system("clear")
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Processing your command...")
        query = recognizer.recognize_google(audio, language='en-UK')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please say that again")
        return "none"
    return query.lower()

def wish():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning, sir! How are you today?")
        speak("Good Morning, sir! How are you today?")
    elif 12 <= hour < 18:
        print("Good Afternoon, sir!")
        speak("Good Afternoon, sir!")
    elif 18 <= hour < 21:
        print("Good Evening, sir!")
        speak("Good Evening, sir!")
    else:
        print("Good Night, sir!")
        speak("Good Night, sir!")

if __name__ == "__main__":
    wish()
    query = take_command()
    if "time" in query:
        current_time = datetime.datetime.now().strftime("[%H:%M:%S %p]")
        print(current_time)
        speak(f"The time is {current_time}")
    elif "firefox" in query:
        speak("Opening Firefox")
        os.system("firefox")
    elif "google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        query = take_command()
        try:
            query = query.replace("google", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Google, ")
            print(results)
            speak(results)
        except Exception as e:
            print(e)
            speak("Not Found Sir")
    elif "youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("http://www.youtube.com")
