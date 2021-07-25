import time

from pygame import mixer

import datetime

mixer.init()

mixer.music.load("water.mp3")
mixer.music.set_volume(1)

inital=datetime.datetime.now()

if inital.hour==(20):
    mixer.music.play()
    if inital.minute==(8):

    if inital.hour==(21):
        mixer.music.stop()
        print("time is up")

while True:
    print("pleas print drank for back ")
    queery=input("  ")
    if queery=="drank":
        mixer.music.stop()
        break

