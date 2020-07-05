from PIL import Image, ImageFilter
import glob
import os



def Blur(path, string):
    for filename in glob.glob(string): #path of raw images
       img = Image.open(filename)
       
       result = img.filter(ImageFilter.BLUR)
    # save blured images to new folder with existing filename
       result.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))


path = 'blured/Ginia munda munda' #path to save
string = 'images/Ginia munda munda/*.jpg' #path to open
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Ginia sublitoralis'
string = 'images/Ginia sublitoralis/*.jpg' 
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Macedopyrgula pavlovici'
string = 'images/Macedopyrgula pavlovici/*.jpg' 
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Macedopyrgula wagneri'
string = 'images/Macedopyrgula wagneri/*.jpg' 
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Ohridopyrgula charensis'
string = 'images/Ohridopyrgula charensis/*.jpg' 
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Ohridopyrgula macedonica'
string = 'images/Ohridopyrgula macedonica/*.jpg'
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

path = 'blured/Ohridopyrgula svnaum'
string = 'images/Ohridopyrgula svnaum/*.jpg' 
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Blur(path, string)

