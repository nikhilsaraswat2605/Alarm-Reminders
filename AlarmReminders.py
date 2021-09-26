import time
from pygame import mixer
initial = time.time()

mixer.init()
mixer.music.load("behti hawa sa tha wo.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()
inp = input("Enter : drank\n")
if inp == "drank":
    mixer.music.stop()
while True:
    final = time.time()
    temp = int(final-initial)
    if temp%(20) is 0:
        mixer.music.play()
        inp = input("Enter : drank\n")
        if inp == "drank":
            mixer.music.stop()
            

        