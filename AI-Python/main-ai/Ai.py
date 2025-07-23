import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import time
from googleapiclient.discovery import build

# gtts and playsound imports
import tempfile
from gtts import gTTS
from playsound3 import playsound

# file imports
from wishMe import *

# Global settings for text-to-speech
USE_GTTS = True  # Set to True to use gTTS, False to use pyttsx3
USE_PLAYSOUND = True  # Set to True to use playsound, False to use


engine = pyttsx3.init('espeak') #engine = pyttsx3.init('sapi5')------>for windows user
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[29].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1.0) 

r = sr.Recognizer()

def speak(text):
    if USE_GTTS:
        try:
            tts = gTTS(text=text, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                if USE_PLAYSOUND:
                    playsound(fp.name, block=True)
                else:
                    engine.say(text)
                    engine.runAndWait()  
        finally:
            time.sleep(0.05)
    else:
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.05)

def basicwishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello sir! good morning")
    elif hour>=12 and hour<17:
        speak("hello sir! good afternoon")
    else:
        speak("hello sir! good evening")
        
def build_search_service(api_key):
    return build('customsearch', 'v1', developerKey=api_key)

def perform_search(search_query, search_service):
    res = search_service.cse().list(
        q=search_query,
        cx='YOUR_CSE_ID'
    ).execute()
    return res['items']

# file creating and saving 

class FileCreatorAI:
    def __init__(self):
        self.files = {}

    def create_file(self, file_name, extension, content, create_path):
        full_file_name = f"{file_name}.{extension}"
        full_file_path = os.path.join(create_path, full_file_name)
        with open(full_file_path, 'w') as file:
            file.write(content)
        self.files[full_file_name] = content
        return f"File '{full_file_name}' created successfully."

    def save_file(self, file_name, save_path):
        if file_name in self.files:
            full_file_path = os.path.join(save_path, file_name)
            with open(full_file_path, 'w') as file:
                file.write(self.files[file_name])
            return f"File '{file_name}' saved at '{full_file_path}'."
        else:
            return f"File '{file_name}' not found."

def recognize_speech_and_get_command():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try: 
        command = r.recognize_google(audio, language='en-in')
        print(f"You said : {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Problem: Did not detect the voice clearly.")
        return
    except sr.RequestError:
        speak("Request failed. Please check your internet connection.")
        return
        
def recognize_speech():
    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio, language='en-in')
        if not command:
            speak("I didn't catch that. Please repeat.")
        print(f"You said:{command}")
        
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

#close command

            if 'close' in command.lower():
                speak("shutting down")
                break
            
#search engine         
                        
            elif 'wikipedia' in command.lower():
                speak('searching wikipedia...')
                command.lower().replace('wikipedia'," ")
                result = wikipedia.summary(command.lower().replace('wikipedia'," "), sentences=20000)
                speak('according to wikipedia')
                print(result)         
                speak(result)
            
# create file and save file
            elif 'create file' in command.lower():
                #file name 
                while True:
                    speak("tell me the name of file")
                    file_name = recognize_speech_and_get_command()
                    if not file_name:
                        speak("I didn't catch that. Please repeat.")
                    else:
                         break
                #file extension
                while True:
                    speak("tell me the extension of file")          
                    extension = recognize_speech_and_get_command()
                    if not extension:
                         speak("I didn't catch that. Please repeat.")
                    else: 
                         break
                #TODO: custom path
                #file path 
                BASE_PATH = "/home/dhyey"
                save_path = None
                while not save_path : 
                    speak("Where do you want to save the file?")
                    print("Options: Desktop, Documents, Downloads, Music, Pictures, Videos")
                    save_path_choice = recognize_speech_and_get_command()
                    
                    if not save_path_choice:
                        speak("I didn't catch that. Please repeat.")
                        continue
                    if 'desktop' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Desktop')
                    elif 'documents' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Documents')
                    elif 'downloads' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Downloads')
                    elif 'music' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Music')
                    elif 'pictures' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Pictures')
                    elif 'videos' in save_path_choice:
                        save_path = os.path.join(BASE_PATH, 'Videos')
                    else:
                        speak("Invalid choice. Please try again.")

                speak("Please type the content for the file.")
                content = input("Enter file content: ")
                creator = FileCreatorAI()
                print(creator.create_file(file_name, extension, content, save_path))

            # elif command == 'save':
            #     file_name = input("Enter file name to save: ")
            #     save_path = input("Enter save path: ")
            #     print(FileCreatorAI().save_file(file_name, save_path))
            
# greetings secition 
            
            elif 'hello' in command.lower():
                    speak('hello how can i help you today?')      
            elif 'who are you' in command.lower():
                    speak('i am ACE. A voice assistent.')     
            elif 'who made you' in command.lower():
                    speak('master dhyey created me')
            elif 'what is your purpose' in command.lower():
                    speak('to surve my master')
            elif 'goodbye' in command.lower(): 
                    speak('goodbye! have a great day!')
                    
#date and time section
                    
            elif 'what is the time' in command.lower():
                    time = datetime.datetime.now().strftime("%H:%M:%S")
                    print(time)
                    speak(f"sir the time is{time}")
            elif 'date' in command.lower():
                    date = datetime.datetime.now().strftime("%Y-%m-%d")
                    print (date)
                    speak(f"sir the date is{date}")
                 
#search engine         
            # TODO: Google search instead of wikipedia
            elif 'wikipedia' in command.lower():
                speak('searching wikipedia...')
                command.lower().replace('wikipedia'," ")
                result = wikipedia.summary(command.lower().replace('wikipedia'," "), sentences=20000)
                speak('according to wikipedia')
                print(result)         
                speak(result)    
                             
#open website section 
    
            elif 'open youtube' in command.lower():
                speak("as you wish. opening youtube")
                webbrowser.open("youtube.com")
            elif 'open instagram' in command.lower():
                speak('as you wish. opening instagram')
                webbrowser.open("instagram.com")
            elif 'open google'in command.lower():
                speak('as you wish. opening google')
                webbrowser.open('google.com')
            elif 'open mail' in command.lower():
                speak('as you wish. opening mail')
                webbrowser.open('gmail.com')  
                
#play music and video section  
              
            elif 'play music' in command.lower():
                music = '/home/dhyey/Music/songs'
                song = os.listdir(music)
                f = random.choice(song)
                print(song)
                os.startfile(os.path.join(music,f))
                
#TODO: make work open application section for linux                 
                
            # elif 'open vs code' in command.lower():
            #     vscode= 'C:\\Users\\dhyey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            #     os.startfile(vscode)
                
            # elif 'open chrome' in command.lower():
            #     chrome= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
            #     os.startfile(chrome)
                
            # elif 'open word' in command.lower():
            #     word = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
            #     os.startfile(word)
                
            # elif 'open excel' in command.lower():
            #     excel = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE""'
            #     os.startfile(excel)
                
            # elif 'open power point' in command.lower():
            #     powerp = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            #     os.startfile(powerp)
                
#to send emails  
            
          #  elif 'send email to riddhi' in command.lower():
              #  try:
                   # discription = listen_and_respond()
                   # to = "riddhikakadiya007@gmail.com"
                  #  sendemail(to, discription)
                  #  speak("your email has been sent.")
                #except Exception as e:
                   # print(e)
                   # speak("Sorry sir! i am not able to send this email")
            
            
            else :       
                speak('i am sorry, i did not understand the command.')
                
                        
        except sr.UnknownValueError:
                speak ('i am sorry, i did not understand what you said.')
        except sr.RequestError as e :
                print(e)
                speak('i am sorry, i was not able to process your command.check your internet connection.')
            

# speak('activating.') 
# speak('          ')
# speak('initializing sequence.')
# speak('          ')
# speak('complete')
basicwishMe()
speak(wishMe(wish)) 
listen_and_respond()