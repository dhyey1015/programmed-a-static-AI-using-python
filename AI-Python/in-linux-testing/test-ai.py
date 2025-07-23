import speech_recognition as sr
import pyttsx3
import time
import tempfile
from gtts import gTTS
from playsound3 import playsound 

USE_GTTS = True  # Set to True to use gTTS, False to use pyttsx3
USE_PLAYSOUND = True  # Set to True to use playsound, False to use pyttsx3

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[29].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0)


def speak(text):
    """Speak out the text using pyttsx3."""
    if USE_GTTS:
        try:
            tts = gTTS(text=text, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                if USE_PLAYSOUND:
                    playsound(fp.name)
                else:
                    engine.say(text)
                    engine.runAndWait()
        finally:
            time.sleep(0.05)
    else:
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.05)
        
def listen_and_respond():
    """Listen to the microphone input and respond"""
    r = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                r.energy_threshold = 300 
                audio = r.listen(source)

            command = r.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
            
            if 'hello' in command.lower():
                speak('Hello, how can I help you today?')      
            elif 'who are you' in command.lower():
                speak('I am ACE, a voice assistant.')     
            elif 'who made you' in command.lower():
                speak('Master Dhyey created me.')
            elif 'what is your purpose' in command.lower():
                speak('To serve my master.')
            elif 'goodbye' in command.lower(): 
                speak('Goodbye! Have a great day!')
                break 
            else:
                speak('I am sorry, I did not understand the command.')
        
        except sr.UnknownValueError:
            speak('I am sorry, I did not understand what you said.')
        except sr.RequestError:
            speak('I am sorry, I could not process your command. Please check your internet connection.')
        except Exception as e:
            print(f"An error occurred: {e}")
            speak('An unexpected error occurred. Please try again.')

speak('Hello, I am ACE, your voice assistant. How may I help you?') 
listen_and_respond()
