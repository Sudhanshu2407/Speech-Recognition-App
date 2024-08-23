import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as py

listener=sr.Recognizer()
engine=pt.init()

def speak(text):
  engine.speak(text)
  engine.runAndWait()
  
def hear():
  try:
    with sr.Microphone() as mic:
      print("...listening..")
      voice=listener.listen(mic)
      cmd=listener.recognize_google(voice)
      cmd=cmd.lower()
      
      if "sudhanshu" in cmd:
        cmd=cmd.replace("sudhanshu","friend")
        print(cmd)

  except:
    pass
  
  return cmd

def run():
  cmd=hear()
  print(cmd)
  if "play" in cmd:
    song=cmd.replace("play"," ")
    speak("playing"+song)
    py.playonyt("playing"+song)   
    
run()
    
  