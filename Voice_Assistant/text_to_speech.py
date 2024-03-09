import pyttsx3
a = pyttsx3.init()
def say(x):
    a.setProperty('rate', 180)
    voices = a.getProperty('voices')
    a.setProperty('voice', voices[1].id)
    a.say(x)
    a.runAndWait()

def stop():
    global a
    a.stop()