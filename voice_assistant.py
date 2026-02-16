import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize Engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Calibrate once for better performance
        r.pause_threshold = 1 
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "none"

speak("System online. How can I help you?")

while True:
    query = listen()

    if "hello" in query:
        speak("Hello Aashish, hope you are having a great day.")

    elif "search for" in query:
        search_query = query.replace("search for", "").strip()
        speak(f"Searching Google for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")

    elif "time" in query:
        time_str = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time_str}")

    elif "exit" in query or "quit" in query:
        speak("Shutting down. Goodbye!")
        break
