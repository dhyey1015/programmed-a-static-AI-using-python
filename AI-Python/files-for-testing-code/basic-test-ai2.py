import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('espeak')#engine = pyttsx3.init('sapi5') 

engine.setProperty('rate',150)    

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen_and_respond():

    r = sr.Recognizer()
    
    while True:
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source)
            
        try:
            command = r.recognize_google(audio, language= 'en-in') 
            print(f"you said : {command}")
            
            # greetings secition 
  
            if 'hello' in command.lower():
                    speak('hello how can i help you today?')      
            elif 'who are you' in command.lower():
                    speak('i am ACE. A voice assistent.')     
            elif 'who made you' in command.lower():
                    speak('master dhyey created me')
            elif 'what is your purpose' in command.lower():
                    speak('to surve my master')
            elif 'goodbye' in command.lower(): 
                    speak('goodbye! have a great day!')
            
            else :       
                speak('i am sorry, i did not understand the command.')

        except sr.UnknownValueError:
                speak ('i am sorry, i did not understand what you said.')
        except sr.RequestError as e :
                speak('i am sorry, i was not able to process your command.check your internet connection.')
                
speak('hello, i am Ace, your voice assistant, how may i help you?') 
listen_and_respond()        
