from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("logfile.txt", "a") as f:
        f.write(f'{msg} {datetime.now()}\n')

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 30*60
    exsecs = 120*60
    eyessecs = 60*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking Time. Please enter 'drank' to stop")
            musiconloop('water.wav', 'drank')
            log_now('drank water at')
            init_water = time()

        if time() - init_eyes > eyessecs:
            print("Eye exercise Time. Please enter 'eyedone' to stop")
            musiconloop('eyes.mp3', 'eyedone')
            log_now('Done eye exercise at')
            init_eyes = time()

        if time() - init_exercise > exsecs:
            print("Physical Exercise Time. Please enter 'exdone' to stop")
            musiconloop('physical.mp3', 'exdone')
            log_now('Physical exercise done at')
            init_exercise = time()
