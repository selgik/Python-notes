#note053_desktop_image_recog.py
import pyautogui


########## 1. HOW DOES AUTOMATION WORK IN PYAUTOGUI
# Treat your screen as screenshotted-image
# In this image, you capture the part of it that you want to apply an action
# For ex. you want system to automatically find 'File' button and click it

#1) let's create variable
file_menu = pyautogui.locateOnScreen("file_menu.png")

#2) partially screen-capture where 'file' exists:
# in Windows: Cntl + Window + s
# in Mac: Command + Shift + 4 
# and save under the name of 'file_menu.png' (same folder where scripts are stored)

#3) let's double check
#system will run to check where that captured 'file' button exists 
print(file_menu)            #ex result: Box(left=73, top=10, width=43, height=36)
pyautogui.moveTo(file_menu) #result: cursor will be moved to the file menu
pyautogui.click(file_menu)  #result: file button will be clicked
                            #if system can't find the image, it will say 'None'

#4) what if you are trying to apply action to changing icon?
# for example, you may want to adjust font size from current(13) to 20 in Paint app
# font sizes change so it is very difficult to save screenshot of it and apply action
# for such case, choose static image and apply relative coordinate to apply action
btn_brush = pyautogui.locateOnScreen("btn_brush.png") #save "Brush" icon near "Text" icon which is static image
pyautogui.click(btn_brush.left-200, btn_brush.top+5000

  
########## 2. locateOnScreen VS locateAllOnScreen
# let's say you are checking on the check-boxes
# there are same, multiple boxes. What to do if you want system to click them all?
# to run below codes as a practice: https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox

#1) save checkbox image under the name 'checkbox.png'
#2) since system needs to repeat the task, use look:
for i in pyautogui.locateAllOnScreen("checkbox.png"):
  print(i)
  pyautogui.click("checkbox.png")
  
#3) if you use locateOnScreen, the first matching image (first checkbox) will only be selected
pyautogui.locateOnScreen("checkbox.png")
pyautogui.click("checkbox.png")


########## 3. ADJUST ACCURACY
# problem: pyautogui is based on image so if resolution or image changes somehow, task may fail
# soltion: in such case, we can adjust accuracy
#          so although all pixel will not match, it will proces the task if certain % matches

#1) in order to adjust accuracy, install new package in terminal:
pip install opencv-python

#2) adjust accuracy in codes and see if it works:
for i in pyautogui.locateAllOnScreen("checkbox.png", confidence=0.9):  #perfect match: 0.99
  print(i)
  pyautogui.click(i)
  
#warning: do NOT drop accuracy too low like 0.1, system may do unexpected and wrong task


########## 4. TUNING THE SPEED
# how pyautogui finds image is like scanning from left top to right, then next line...etc
# so if the image you are tying to find is located on the right bottom side, it will take longer time 
# there are 2 ways to improve speed for below:
trash_icon = pyautogui.locateOnScreen("trash_icon.png")
pyautogui.moveTo(trash_icon)

#1) grayscale
# by changing color to grayscale, 30% speed improvement is expected according to document
trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale = True)
pyautogui.moveTo(trash_icon)

#2) assining the range for search
# first, find out coordainte of range you want to assign, using pyautogui.mouseInfo()
# let's say the range(box)'s top left coordiante is (1570, 54)
# and right bottom is (1886, 122)

# assign range in codes:
# range(left, top, width, height)
trash_icon = pyautogui.locateOnScreen("trash_icon.png", range=(1570, 54, 1886-1570, 122-54))
pyautogui.moveTo(trash_icon)


########## 5. STANDBY AND PROCESS RPA
# sometimes, you have to make RPA wait(or standby) until certain task is completed
# situation: you want to click menu botton of the notepad.
#            (I have already screen-captured menu button in the notepad and saved)
# result:    codes returned "failure" as it could not wait while I was opening notepad program 
#            in this case, you need RPA to wait until program is loaded (appears on the screen)

file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")

if file_menu_notepad:
  pyautogui.click(file_menu_notepad)
else:
  print("failure")

#1) while
#while file_menu_notepad is None, try to find it and print failure. if fount, click menu
file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")

while file_menu_notepad is None:
  pyautogui.locateOnScreen("file_menu_notepad.png")
  print("failure")  
pyautogui.click(file_menu_notepad)

#2) count time
import time
import sys

timeout = 10        #standby 10 seconds
start = time.time() #start time setting

file_menu_notepad = None
while file_menu_notepad is None:                    
  file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png") 
  end = time.time()                                 #--> while file_menu_notepad is None, count time
  if end - start > timeout:                         #--> if more than 10s past and still couldn't find file_menu_notepad?
    print("finish")                                 #--> print 'finish' and end sys
    sys.exit()
                                                    #--> if within 10 sec (within while), file_menu_notepad was found?
pyautogui.click(file_menu_notepad)                  #--> click file_menu_notepad
          
#3) converting above into functions for future use:
#create two funcion: (a) find image within certain time (b) if image if found, click it
#(a) find image within certain time
def find_target(img_file, timeout=30):
  start = time.time()
  target = None
  while target is None:
    target = pyautogui.locateOnScreen(img_file)
    end = time.time()
    if end - start > timeout:
      break
  return target #at this point, target will either be None or pyautogui.locateOnScreen(img_file)

#(b) if image if found, click it
def my_click(img_file, timeout=30):
  target = find_target(img_file, timeout)
  if target:
    pyautogui.click(target)
  else:
    print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
    sys.exit()

#now, let's run functions:
my_click("file_menu_notepad.png", 10)

  
