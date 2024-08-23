import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk
import webbrowser

# Initialize recognizer and engine
listening = sr.Recognizer()
engine = pt.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to hear and process voice commands
def hear():
    try:
        with sr.Microphone() as mic:
            # Adjust for ambient noise to improve accuracy
            listening.adjust_for_ambient_noise(mic, duration=1)
            print('Listening...')
            voice = listening.listen(mic)
            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()
            if 'siri' in cmd:
                cmd = cmd.replace('siri', '').strip()
                print(f"Command received: {cmd}")
                return cmd
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand your voice. Please repeat.")
    except sr.RequestError as e:
        speak(f"Could not process your request; {e}")
    return ""

# Main function to process commands
def process_command(cmd):
    if 'play' in cmd:
        song = cmd.replace('play', '').strip()
        speak(f'Playing {song} on YouTube.')
        pk.playonyt(song)
    
    elif 'search' in cmd:
        query = cmd.replace('search', '').strip()
        speak(f'Searching {query} on Google.')
        pk.search(query)
    
    elif 'open' in cmd:
        site = cmd.replace('open', '').strip()
        if not site.startswith('http://') and not site.startswith('https://'):
            site = f'http://{site}'
        speak(f'Opening {site}.')
        webbrowser.open(site)

    elif 'time' in cmd:
        from datetime import datetime
        current_time = datetime.now().strftime('%I:%M %p')
        speak(f'The current time is {current_time}.')
        print(f'The current time is {current_time}.')
    
    else:
        speak("I didn't catch that. Can you please repeat?")

# Run the voice assistant
if __name__ == "__main__":
    while True:
        command = hear()
        if command:
            process_command(command)
        else:
            speak("No command detected. Please try again.")
