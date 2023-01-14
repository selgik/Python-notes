#note052_desktop_screen.py
import pyautogui


########## 1. TAKE A SCREENSHOT
img = pyautogui.screenshot()    #take a screenshot
img.save("screenshot.png")      #save under the title 'screenshot'


########## 2. COMPARE PIXEL(RBG)
#1) let's find out the RBG of blue-colored-status remark next to my icon in github
pyautogui.mouseInfo()           #capture mouseinfo (ex. 30,20,45,129,185 #2E81B9)

pixel = pyautogui.pixel(30,20)  #let's double check, add coordinate and see the results
print(pixel)                    #result: (45,129,185)

#2) how can you use pixel info?
print(pyautogui.pixelMatchesColor(30,20,(46,129,185)))  
print(pyautogui.pixelMatchesColor(30,20,pixel))       #same as above
      
## above code will compare whether RBG of coordinate(30,20) is same as RBG(46,129,185)
## since they are the same, result will show as True
## how can we use pixelMatchesColor?
## --> ex. let's say you might be creating a program where some kind of button will show green
##         if login and password matches to that of record. 
##         if color matches, you can (=login successful) you write codes further or stop if it fails.

  
