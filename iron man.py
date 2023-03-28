
import webbrowser
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import os ,sys ,subprocess
import smtplib
from requests import get
import pyjokes
import pyautogui 
import time
import json
engine= pyttsx3.init('nsss')
voices=engine.getProperty('voices')
print(voices[4].id)
engine.setProperty('voice',voices[7].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()
    


def wisme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("good morning")
        speek("good morning")
        
    elif hour>=12 and hour<=18:
        print("good afternoon")
        speek('good afternoon ')
        
    else:
        print("good evenig")
        speek("good evening")
    print("hello sir  i am jarvis , how may i help you")
    speek("hello sir  i am jarvis , how may i help you")


def teke():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio=r.listen(source)
         
    try:
     print("reconizing...")
     query = r.recognize_google(audio, language='en-in')
     print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("say again please...")
        return "None"        
    return query 



def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('dev19stormbreaker@gamil.com','your-password')
    server.sendmail('your gamilID@gamil.com',to,content)
    server.close()


def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=5c9549b425a0420eb1e7e5cc70b579b6"
    main_page = requests.get
    #print(main_url)
    articles = main_page["articles"]
    #print(articles)
    head =[]
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's{day[i]} nesw is:",head[i])
        speek(f"today's{day[i]} nwes is {head[i]}")    
if __name__ ==  "__main__":
    #speek("hello world welcome")
    wisme()
    while True:
        query = teke().lower()
        if 'wikipedia' in query:
            speek('searching in wikipedia')
            query = query.replace("wikipeadia","")
            results = wikipedia.summary(query,sentences =5)
            speek("according to wikipedia")
            print(results)
            speek(results)
        elif 'open youtube' in query:
            speek("sir what should i search in Youtube ")
            cm = teke().lower()
            url="https://www.youtube.co.in/search?q="
            search_url = url+cm
            webbrowser.open(search_url)

        elif 'open google' in query:
            speek("sir what should i search in Google for you")
            cm = teke().lower()
            url= "https://google.co.in/search?q="
            search_url = url+cm
            webbrowser.open(search_url)
        elif 'open instagram' in query:
            webbrowser.open("https://instagram.com")
        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")
        elif 'play music' in query:
            speek("sir what would you like to listen")
            song= teke().lower()
            speek("sir playing"+song+"    for you relax and enjoy it")
            url="https://open.spotify.com/search/?q="
            search_url=url+song
            webbrowser.open(search_url)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speek(f"sir the time is{strTime}")
        elif'open code' in query:
            subprocess.call(r"/Applications/PyCharm CE.app") 
        elif 'email to dev' in query:
            try:
                speek("whai should i say ")
                content = teke()
                to = "dev19stormbreaker@gamil.com"
                sendEmail(to,content)
                speek("email has been send")
            except Exception as e :
                print(e)
                speek("sorry mail could not sent")
        elif  'ip addres' in query :
            ip = get("https://api.ipify.org").text 
            print("sir your IP addres is.....   ",ip)
            speek(f"sir your is IP addres is {ip}\n")
        elif ' tell me joke' in query:
            joke = pyjokes.get_joke(language="en",category="all")
            speek(joke)    

        elif 'ok close' in query:
            speek("ok sir closing chome")
            os.system("taskkill /f /im Google chrom")   
        elif 'ok off ' in query:
            speek("thanks for using me , have a good day sir ") 
            sys.exit()   
        elif 'switch tab' in query:
            pyautogui.keyDown('f3')
            pyautogui.press('control'+'right')
            time.sleep(1)
            pyautogui.keyUp('f3')
        elif 'tell the news' in query:
            speek("please wait sir,fetching the letest news ")
            news()