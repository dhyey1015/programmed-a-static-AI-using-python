import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        command = recognizer.recognize_google(audio, language= 'en-in') 
        if 'create file' in command.lower():
            text = recognizer.recognize_google(audio)
            return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
    return None

# Call the function and store the result in a variable
voice_input = recognize_speech()

if voice_input:
    print("You said:", voice_input)
else:
    print("Failed to recognize speech.")
