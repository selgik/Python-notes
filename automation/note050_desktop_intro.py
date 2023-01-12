#note050_desktop_intro.py


########## 1. INSTALL PACKAGE
pip install pyautogui
import pyautogui

########## 2. LET'S TEST OUT!
size = pyautogui.size()
print(size)     #result: current screen size --> Size(width=1920, 1080)

size[0]         #this will be width 
size[1]         #this will be height

########## 2. HOW DOES IT WORK
# how does automation work in pyautogui? 
# treat your desktop screen as an 'image'. In order to tell system to go to certain point, click and drag etc.,
# you need to tell system a corresponding point, which is 'width' and 'height' of your screen.
# that's why width/height is needed.

pyautogui.mouseInfo()  
#a program will appear which will give all the information of a mouse point
#such as width, height, HEX color etc.
  
    
