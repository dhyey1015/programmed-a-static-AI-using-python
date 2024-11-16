import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

from googleapiclient.discovery import build





engine = pyttsx3.init('espeak') #engine = pyttsx3.init('sapi5')------>for windows user
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[28].id)
engine.setProperty('rate', 150)

r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
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

    def create_file(self, file_name, extension, content):
        full_file_name = f"{file_name}.{extension}"
        with open(full_file_name, 'w') as file:
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
        
def recognize_speech():

    with sr.Microphone() as source:
        audio = r.listen(source)



        
    
        
def listen_and_respond():
    
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
                
                #speak("tell me the name of file")
                file_name = r.recognize_google(audio)
                #speak("tell me the extension of file")          
                extension = r.recognize_google(audio)
                content = input("Enter file content: ")
                print(FileCreatorAI().create_file(file_name, extension, content))

            elif command == 'save':
                file_name = input("Enter file name to save: ")
                save_path = input("Enter save path: ")
                print(FileCreatorAI().save_file(file_name, save_path))
            
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
                
# open application section                  
                
            elif 'open vs code' in command.lower():
                vscode= 'C:\\Users\\dhyey\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(vscode)
                
            elif 'open chrome' in command.lower():
                chrome= 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(chrome)
                
            elif 'open word' in command.lower():
                word = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
                os.startfile(word)
                
            elif 'open excel' in command.lower():
                excel = '"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE""'
                os.startfile(excel)
                
            elif 'open power point' in command.lower():
                powerp = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(powerp)
                
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
wishMe()
speak('what can i do for you') 
listen_and_respond()