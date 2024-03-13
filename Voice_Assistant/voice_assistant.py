import pyttsx3 as p
import speech_recognition as sr
import wikipedia as wkp
import youtube as yt
import randfacts
import jokes
import datetime

e = p.init()
r = sr.Recognizer()
text = ""
rate = e.getProperty('rate')
e.setProperty('rate', 180)
v = e.getProperty("voices")
e.setProperty('voice', v[1].id)

def prg_say(t):
    e.say(t)
    e.runAndWait()

def wishing():
    h = int(datetime.datetime.now().hour)
    if (h > 0 and h < 12):
        return ("morning")
    elif (h >= 12 and h < 16):
        return ("afternoon")
    else:
        return ("evening")

def listening():
    with sr.Microphone() as s:
        global text
        text = ""
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(s, 1.2)
        print("listening..")
        audio = r.listen(s)
        try:
            text = r.recognize_google(audio)
        except:
            if (text == ""):
                prg_say("I didn't catch it")
                listening()
        print(text)

today_dt = datetime.datetime.now()
prg_say("Good" + wishing() + " sir, I am your voice assistant")
prg_say("Today is, " + today_dt.strftime('%d') + " of " + today_dt.strftime('%B') + " and its currently " + (today_dt.strftime('%I')) + (today_dt.strftime('%M')) + (today_dt.strftime('%p')))
prg_say("How are you?")
        
listening()
if ("not") in text:
    prg_say("What happened sir")
elif "what about you" and "you" in text:
    prg_say("I am also having good day")

prg_say("What can I do for you?")
while True:
    print("""\nGive some information.
Play a video.
Give some interesting facts
Tell a joke""")
    listening()
    if "information" in text:
        prg_say("On which topic you need information?")
        listening()
        print("Searching {} on wikipedia".format(text))
        prg_say("Searching {} on wikipedia".format(text))
        a = wkp.info()
        a.get_info(text)
        a.keep_open_forever()
        a.close()
    elif ("play" or "video") in text:
        prg_say("You want me to play which vedio?")
        listening()
        print("Playing {} on youtube".format(text))
        prg_say("Playing {} on youtube".format(text))
        a = yt.music()
        a.play(text)
        a.keep_open_forever()
        a.close()
    elif ("fact" or "facts") in text:
        prg_say("Sure sir, ")
        fact = randfacts.get_fact()
        print(fact)
        prg_say("Do you know, " + fact)
    elif ("joke" or "jokes") in text:
        prg_say("Sure sir, ")
        j = jokes.joke()
        print(j[0])
        prg_say(j[0])
        print(j[1])
        prg_say(j[1])
    

    prg_say("Let me know if you need more assistance")
    listening()
    if ("no" or "nothing" or "thanks you" or "that's it") in text:
        break
    prg_say("What can I do for you?")