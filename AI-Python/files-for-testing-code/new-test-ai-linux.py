import speech_recognition as sr
import pyttsx3

def initialize_audio():
    engine = pyttsx3.init()
    # Configure for your specific audio device
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    return engine

def main():
    # Initialize the recognizer and engine
    recognizer = sr.Recognizer()
    engine = initialize_audio()
    
    # Explicitly specify the microphone device index
    try:
        # List available microphones
        mics = sr.Microphone.list_microphone_names()
        print("Available microphones:")
        for i, mic in enumerate(mics):
            print(f"{i}: {mic}")
        
        # Use device_index=1 for the sof-hda-dsp analog input
        with sr.Microphone(device_index=1) as source:
            print("\nAdjusting for ambient noise... Please be quiet.")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Ambient noise adjustment complete.")
            
            # Test text-to-speech
            engine.say("Audio system is ready")
            engine.runAndWait()
            
            print("\nListening... Say something!")
            audio = recognizer.listen(source)
            
            try:
                text = recognizer.recognize_google(audio)
                print(f"\nYou said: {text}")
                engine.say(f"You said: {text}")
                engine.runAndWait()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure your microphone is not muted in system settings")
        print("2. Check if the correct microphone is selected in your system's sound settings")
        print("3. Try running 'pavucontrol' to check audio levels")

if __name__ == "__main__":
    main()