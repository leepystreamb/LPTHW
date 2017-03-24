import numpy as np
import cv2


print "Please type in the filename of your horror movie"
print "help: put the video file in the same folder as this programme or type the path of the video file."
print " e.g. 'example.mp4' or 'C:/user/document/example.mp4'"
print "Press Q to exit the preview."
filename = raw_input('> ')

cap = cv2.VideoCapture(filename)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # fourcc codecs
width = int(cap.get(3)) # get the property from the source video
height = int(cap.get(4)) # same as above
framerate = cap.get(5) # same as above
out = cv2.VideoWriter('out.avi', fourcc, framerate, (width, height)) # outputing the result video,
# please edit the fourcc code if using different compilers and os

while(cap.isOpened()):

    ret, frame = cap.read()


    b, g, r = cv2.split(frame) # editing the color
    r = r + 30
    g = g + 10
    b = b + 5
    warm = cv2.merge((b, g, r))

    h, s, v = cv2.split(cv2.cvtColor(warm, cv2.COLOR_BGR2HSV)) # editing saturation
    s = s + 30
    sat = cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)




    blur = cv2.blur(sat, (20,20)) # adding a bluring filter and overlaying it on the original
    dst = cv2.addWeighted(sat, 0.3, blur, 0.7, 0)
    cv2.imshow('preview', dst) # preview window



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
