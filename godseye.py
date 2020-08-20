import os
import pyttsx3
import subprocess
import time
import datetime
from nltk.tokenize import word_tokenize

#settings,calculator
engine = pyttsx3.init()
engine.say("welcome to god's eye")
engine.runAndWait()
os.system('cls')

def check(x):
    tokens = word_tokenize(x.lower())
    if (("run" in tokens) or ("execute" in tokens ) or ("open" in tokens) or ("search" in tokens) or ("quit" in tokens)or ("exit" in tokens)):
        return True
    else:
        return False
    
print("     ____ _____  ____/ /____   ___  __  _____ ")
print("    / __ `/ __ \/ __  / ___/  / _ \/ / / / _ \ ")
print("   / /_/ / /_/ / /_/ (__  )  /  __/ /_/ /  __/")
print("   \__, /\____/\__,_/____/   \___/\__, /\___/ ")
print("  /____/                         /____/       ")
print("------------------------------------------------")

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

while True:
    print("\nHow can i help you? ")
    user = input()
    if ("dont" in user or "not" in user):                                   #not,dont
        pass
    elif("--help" in user):
        print('''*********Help for godseye********
        
a CLI based assistant written in python 3.7.6

usage -
type '--help' for this output
say 'hello' to godseye
ask 'what is your name?'
ask for date or time
exceptable keywords for running programs - run, execute, open
exclusive commands - enable wifi, disable wifi, search [query], shutdown, restart, exit, quit, open [folder name]

Developed by - Viplove Bansal 
''')
    elif("hello" in user):                                                  #hello
        speak("hello, how can i help you?")
    elif("your" in user or "name" in user):                                 #name
        speak("my name is god's eye")
    elif("time" in user):                                                   #time
        speak("current time is ")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(current_time)
    elif("date" in user):                                                   #date
        ct = datetime.datetime.now()
        print(ct)
    else:
        if ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("chrome" in user) and check(user) == True):            #Chrome 
            speak("opening, chrome")
            os.system("start chrome")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("notepad" in user) and check(user) == True):         #notepad
            speak('opening notepad')
            os.system("notepad")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("vs code" in user) and check(user) == True):         #visual studio code
            speak("opening, vs code")
            os.system("start code")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("media player" in user) and check(user) == True):    #windows media player
            speak("opening windows media player")
            os.system("start wmplayer")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("youtube" in user) and check(user) == True):         #youtube in default browser
            speak("opening, youtube")
            os.system("start explorer http://youtube.com")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("google" in user) and check(user) == True):          #google in deafult browser
            speak("opening, google")
            os.system("start explorer http://google.com")
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("facebook" in user) and check(user) == True):        #facebook in default browser
            speak("opening, facebook")
            os.system("start explorer http://facebook.com")
        elif (("run" in user) and ("url" in user) and check(user) == True):                                                             #runs specified url
            x = user[8:]
            speak("running url")
            os.system("start explorer http://{}".format(x))
        elif ("open" in user and check(user) == True):                                                #opens file/folder
            y = user[5:]
            os.system("C: && start {}".format(y))
        elif(("enable" in user) and ("wifi" in user)):                                                #enable wifi
            speak("enabling wifi")
            #change file path for wifi_enable
            subprocess.call([r'E:\users\tr\Desktop\wifi_enable.bat'])
        elif(("disable" in user) and ("wifi" in user)):                                               #disable wifi
            speak("disabling wifi")
            #change file path here for wifi_disable
            subprocess.call([r'E:\users\tr\Desktop\wifi_disable.bat'])
        elif(("search" in user) and check(user) == True):                                             #search on google
            q = user[7:]
            speak("searching on google")
            os.system("start explorer \"http://www.google.com/search?q={}\"".format(q))
        elif(("shutdown" in user)):
            os.system("SHUTDOWN /s")
        elif(("restart" in user)):
            os.system("SHUTDOWN /r")
        elif (("quit" in user) or ("exit" in user) and check(user) == True):                           #quiting
            speak("terminating in 3, 2, 1")
            exit()
        elif ((("run" in user) or ("execute" in user ) or ("open" in user)) and ("cal" in user) and check(user)==True):             #calculator
            os.system("calc")
        else:                                                                                           #unsupported input
            print("\n**Unsupported input**\n")
    
