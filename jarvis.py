
import datetime
import pyttsx3
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
#print(voices[2].id) 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good mornig sir")
    elif hour>=12 and hour<=18:
        speak("Good after noon sir ")
    else:
        speak("Good evenig sir")
    speak("hello sir I am jarvis. please tell me how i may help you ")            

if __name__ == "__main__":
    wishme()