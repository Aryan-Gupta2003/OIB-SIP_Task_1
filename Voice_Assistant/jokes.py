import requests as r

u = "https://official-joke-api.appspot.com/random_joke"
jd = r.get(u).json()

array = ["",""]
array[0] = jd["setup"]
array[1] = jd["punchline"]

def joke():
    return array