import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('espeak')
engine.setProperty('rate', 150) 

def speak(text):
    """Speak out the provided text using pyttsx3."""
    engine.say(text)
    engine.runAndWait()
    
def listen_and_respond():
    """Listen to the microphone input and respond based on predefined commands."""
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
