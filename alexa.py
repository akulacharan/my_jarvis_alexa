from multiprocessing import Process
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyglet

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
# setting rate of speech
engine.setProperty('rate',120)
#print(rate)
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! sir")

    else:
        speak("Good Evening! sir")




def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.5
        audio = r.record(source,duration=5)

        try:
            print('recognizing...')
            query = r.recognize_google(audio,language='en-in')
            print('user said:{}'.format(query))

        except Exception as e:
            print(e)
            print("say that again please...")
            return "None"
        return  query


def func1():
    while True:

        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query


        if "wikipedia" in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                pass

        elif 'hi' in query:
            speak('hi there how can i help you sir')
            continue

        elif 'wish' in query:
            wishme()
            continue

        elif 'your name' in query:
            speak('Iam Alexa your friend')
            continue

        elif 'miss you' in query:
            speak('miss you tooo cherry')
            continue
        elif 'love' in query:
            speak('Love you tooo cherry')
            continue

        elif 'open youtube' in query:
            speak('ok sir')
            webbrowser.open("https://www.youtube.com")


        elif 'open stack overflow' in query:
            speak('ok sir')
            webbrowser.open("https://www.stackoverflow.com")


        elif 'open google' in query:
            speak('ok sir')
            webbrowser.open("https://www.google.com")

        elif 'open gmail' in query:
            speak('ok sir')
            webbrowser.open("https://mail.google.com/")

        elif 'close chrome' in query:
            speak('ok sir closing chrome')
            os.system("TASKKILL /F /IM chrome.exe")

        elif 'whatsapp' in query:
            speak('ok sir whatsapp')
            webbrowser.open("https://web.whatsapp.com/")


        elif 'music' in query:
            if 'open music' in query:
                speak('ok sir')
                music_dir = 'E:\music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'close music' in query:
                speak('ok sir closing vlc player' )
                os.system("TASKKILL /F /IM vlc.exe")

            #webbrowser.open("https://www.youtube.com/watch?v=DIQQfo3ZAvo")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "owner" in query:
            speak('He is cherry, yes he is the genius who made me')


        elif 'code' in query:
            if 'open code' in query:
                speak('ok sir opening pycharm')
                codePath ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
                os.startfile(codePath)
            elif 'close code' in query:
                speak('ok sir closing pycharm')
                os.system("TASKKILL /F /IM PyCharm64.exe")

        elif 'telegram' in query:
            codepath = "C:\\Users\\KARTHIK\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            if 'open telegram' in query:
                speak('ok sir')
                os.startfile(codepath)
            elif 'close telegram' in query:
                speak('ok sir')
                os.system("TASKKILL /F /IM Telegram.exe")

        elif 'notepad' in query:
            codepath = "C:\\Windows\\System32\\notepad.exe"
            if 'open notepad' in query:
                speak('ok sir')
                os.startfile(codepath)
            elif 'close notepad' in query:
                speak('ok sir closing notepad')
                os.system("TASKKILL /F /IM Notepad.exe")


        elif 'git' in query:
            codepath = "C:\\Users\\KARTHIK\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
            if 'open git' in query:
                speak('ok sir')
                os.startfile(codepath)
            elif 'close git' in query:
                speak('ok sir closing github')
                os.system("TASKKILL /F /IM GitHubDesktop.exe")

        elif 'control' in query:
            codepath = "C:\\Windows\\System32\\control.exe"
            speak('ok sir')
            os.startfile(codepath)

        elif 'manager' in query:
            codepath = "C:\\Windows\\System32\\taskmgr.exe"
            speak('ok sir task manager')
            os.startfile(codepath)

        elif 'prompt' in query:
            codepath = "C:\\Windows\\System32\\cmd.exe"
            speak('ok sir command prompt')
            os.startfile(codepath)
        
        elif 'python' in query:
            if 'open python' in query:
                codepath = "C:\\Users\\KARTHIK\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
                speak('ok sir opening python')
                os.startfile(codepath)
            elif 'close python' in query:
                speak('closing python')
                os.system("TASKKILL /F /IM Python.exe")

        elif 'cleaner' in query:
            if 'open cleaner' in query:
                codepath = "C:\\Program Files (x86)\\cmcm\\Clean Master\\cmtray.exe"
                speak('ok sir clean master')
                os.startfile(codepath)
            elif 'close cleaner' in query:
                speak('closing clean master')
                os.system("TASKKILL /F /IM cmtray.exe")


        elif 'log off' in query:
            speak('do you want to logoff sir')
            if 'yes log off' in query:
                speak('ok sir logging off bye')
                os.system("shutdown /l")
            else:
                continue


        elif 'restart' in query:
            speak('do you want to restart sir')
            if 'yes restart' in query:
                speak('ok sir shtting down bye')
                os.system("shutdown /r")
            else:
                continue

        elif 'switch off' in query:
            speak('do you want to shut down sir')
            if 'yes switch off' in query:
                speak('ok sir shtting down bye')
                os.system("shutdown /s")
            else:
                continue

        elif 'quit' in query:
            speak('ok sir see you later')
            exit()


def func2():

    animation = pyglet.image.load_animation('jar.gif')
    animSprite = pyglet.sprite.Sprite(animation)

    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r, g, b, alpha = (0.5, 0.5, 0.8, 0.5)

    pyglet.gl.glClearColor(r, g, b, alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()


    pyglet.app.run()









if __name__ == '__main__':
    speak('your request sir how may i help you')
    pass
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()













