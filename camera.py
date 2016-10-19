#!/usr/bin/python
# The programs run on RBp.
# It call the folder's name and take a pics.
# After terminated, it makes a zip.
import os
import shutil
# Getch on python https://goo.gl/jeLuDv
from getch import getch
from time import sleep
from picamera import PiCamera
num = 400
camera = PiCamera()
camera.resolution = (640,480) #https://goo.gl/E5EJ22

#Main's program
print 'Raspberry script'
dirName = raw_input('Enter name s dir: ')
os.makedirs(dirName)
print "Directory created."
os.chdir("/home/pi/"+dirName)
print 'SPACEBAR for shoot & ESC for terminate'
num=400
while True:
    key = getch()
    key = ord(key)
    if key == 27: #ESC
        break
    if key == 32: #spacebar
        # Camera warm-up time
        sleep(2)
        # https://goo.gl/qKukJU
        nome_img=str(num)+'.jpeg'
        num=num+5
        camera.capture(nome_img)
        print 'scattato.'
print "Acquisizione completata."
shutil.make_archive('/home/pi/'+dirName, 'zip', '/home/pi/'+dirName)
print "Zipped."
