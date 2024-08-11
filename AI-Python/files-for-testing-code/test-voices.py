# import pyttsx3

# engine = pyttsx3.init('espeak') #engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print("vpocdm",voices)

# engine.setProperty('voice',voices)


# engine = pyttsx3.init()
# voice = engine.getProperty('voices')

# engine.setProperty('rate',200) 
# engine.setProperty('voices', voice[1].id) 

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# List all voices with their IDs and languages
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Languages: {voice.languages}")
    print(f" - Gender: {voice.gender}")
    print(f" - Age: {voice.age}")
    print("\n")