from moviepy.editor import *
from random import randint
import numpy as np

print "Please type in the filename of your horror movie"
print "help: put the video file in the same folder as this programme or type the path of the video file."
print " e.g. 'example.mp4' or 'C:/user/document/example.mp4'"
filename = raw_input('> ')

songlist = ['01.mp3', '02.mp3', '03.mp3']
clip = VideoFileClip(filename)
clip = clip.volumex(0.2)



while True:
    try:
        print "What vibe are you feeling?"
        print "Please select the correspondent number."
        print "-1. Dreamy   -2. Excited     -3. Funky   -4. Random"
        songchoice = raw_input('> ')
        x = int(songchoice)
        break
    except ValueError:
        print "Please enter a valid number!"

if '1' in songchoice:
    song = AudioFileClip(songlist[0])
elif '2' in songchoice:
    song = AudioFileClip(songlist[1])
elif '3' in songchoice:
    song = AudioFileClip(songlist[2])
elif '4' in songchoice:
    song = AudioFileClip(songlist[randint(0,3)])
else:
    print "please enter a valid number."
    songchoice = raw_input('> ')

final = CompositeVideoClip(clip)
final.set_audio(audio.set_duration(final))
final.write_videofile("output.mp4", codec='libx264')
