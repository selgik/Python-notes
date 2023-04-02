#exercise006(desktop).py
#prepare libraries and settings

import pyautogui

##### Scenario: Write codes to automate below tasks
#1. Run Paint program and then maximize the app screen
#2. Anywhere in the canvas, type "great job"
#3. Wait for 5 seconds and finish Painter without saiving it


##### 1. MY VERSION
#1. Run Painter program and then maximize the app screen
pyautogui.hotkey("super", "r")  #open terminal
pyautogui.write("mspaint")      #type mspainter
pyautogui.hotkey("enter")
pyautogui.sleep(2)
pyautogui.hotkey("super", "up") #maximize screen 

#2. Anywhere in the canvas, type "great job"
button = pyautogui.locateOnScreen("mspaint-a.pang")   #search "Text" icon as screenshotted and saved under mspaint-a.png 
pyautogui.moveTo(button)        #go to that icon
pyautogui.click(button)         #click that icon

pyaugotui.moveTo(697, 650)      #coordinate can be anything within the canvas
pyautogui.click()
pyautogui.write("Great Job") 

#3. Wait for 5 seconds and finish Painter without saiving it
pyautogui.sleep(5)
pyautogui.hotkey('alt', 'f4')   #close active window (which is Pait app)
pyautogui.sleep(2)

button2 = pyautogui.locateOnScreen("mspaint-ds.png", confidence=0.8)  #search "Do Not Save" icon as screenshotted and saved under mspaint-a.png 
pyautogui.moveTo(button2)
pyautogui.click(button2)


##### 2. CODE REVIEW
# Comparing to my codes, instructor's codes look easier for maintenance.
# If scenario would be changed (or get more complex), I may have to review and re-write a lot 
# but instructor's one contain functions and if statememnt hence it will be eaiser to navigate and carry maintenance. 
# For simple automation, my codes might be shorter and better but for complex scenario, instruction one looks better


##### 3. INSTRUCTOR'S VERSION
import sys
import pyperclip

#1. Run Paint program and then maximize the app screen
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")
pyautogui.sleep(2)  #wait until program comes up

window = pyautogui.getWindowsWithTitle("Untitled - Paint")[0]   #get window having title "Untitled-Paint" assuming there is 1 active Paint window
if window.isMaximised == False:
  window.maximize()

#2. Anywhere in the canvas, type "great job"
pyaugotui.sleep(2)
bnt_txt = pyautogui.locateOnScreen("mspaint-a.png", confidence = 0.8) #search "Text" icon as screenshotted and saved under mspaint-a.png 
if btn_txt:                                                           #if "Text" icon exists, click it; otherwise close the program
  pyautogui.click(btn_txt, duration=0.5)    #duration added to slow down mouse movement
else:
  print("Failure")
  sys.exit()

def my_write(text):                         #if you need to type other character than alphabet, you need pyperclip
  pyperclip.copy(text)
  pyaugotui.hotkey("ctrl", "v")
  
my_write("참 잘했어요!")

#3. Wait for 5 seconds and finish Painter without saiving it
pyautogui.sleep(5)
window.close()
pyautogui.sleep(0.5)  #in case pop up comes up late, let's give some time
pyaugotui.press("n")  #do not save

  
