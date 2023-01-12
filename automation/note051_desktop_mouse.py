#note051_desktop_mouse.py
import pyautogui


########## 1. MOUSE MOVEMENT
#1) move mouse to certain point of your screen
#(x,y) starts from x=0, y=0 which is top left corner of the screen.
pyautogui.moveTo(200,100)                 #move mouse to width=200, height=100 from (0,0)
pyautogui.moveTo(200,100, duration=0.25)  #during 0.25 seconds, move to width=200, height=100 (mouse will move slower)

#2) moveTo vs move
#moveTo: absoluate coordinates vs move: relational coordinates
pyautogui.moveTo(100,100, duration=5)
pyautogui.moveTo(200,200, duration=5)     #from (0,0) move to width=200, height=200
pyautogui.moveTo(300,300, duration=5)     #from (0,0 move

#above codes are same as below:
pyautogui.move(100,100, duration=5)
pyautogui.move(100,100, duration=5)       #from the mouse point, move +100 width and +100 height
pyautogui.move(100,100, duration=5)       #same as above

#3) let's check the coordinates
pyautogui.sleep(3)                        #give delay so that you can move your mouse to designated place
print(pyautogui.position())               #result ex: Point(x=1224, y=478)

p = pyautogui.position()
print(p[0], p[1])                         #result ex: 1224 478
print(p.x, p.y)                           #result ex: 1224 478


########## 2. MOUSE ACTION
#1) click (excercise: click 'file' button)
pyautogui.sleep(3)                        #move your mouse to file button to read coordinates
print(pyautogui.position())               #read coordinates
pyautogui.click(97, 22, duration=1)       #input coordinates inside click()

#2) click() = mouseDown() + mouseUp()
# click action is combination of mouseDown(hold mouse click) and mouseUp(take off)
# when to use mouseDown? for dragging action!
# excercise: let's draw a line in the paint program using above
pyautogui.sleep(3)                        #give few moments so that you can run codes and open paint program in front            
pyautogui.moveTo(260, 565)                #move to the canbas
pyautogui.mouseDown()                     #hold mouse(prepare to draw)
pyautogui.moveTo(360, 588)                #move, so that line can be drawn
pyautogui.mouseUp()                       #finish. Result: a line will be drawn

#3) drag
# dragTo() vs drag(): absolute point vs relational point
# excercise: let's drag paint program to the right side
pyautogui.sleep(3)                        
pyautogui.moveTo(1176, 377)
pyautogui.drag(100, 0, duration=0.25)

#4) double click
pyautogui.doubleClick()
pyautogui.click(clicks=2)     #this works same as double click
pyautogui.click(clicks=500)   #when to use? ex. when you need to create macro program

#5) right click, middle click
pyautogui.rightClick()        #right click
pyautogui.middleClick()       #mouse's wheer click

#5) scroll
pyautogui.scroll(500)         #scroll up
pyautogui.scroll(-500)        #scroll down


########## 3. DELAY OR BREAK AUTOMATION
#1) manuallly breaking the codes
# Problem: unlike other Python codes, pyautogui might not be stopped with usual Ctnl+C.
# Solution: move your mouse to either corner of the screen (ex. bottom right)
for i in range(1,10):
  pyautogui.move(100,100)
  pyautogui.sleep(1)          #action will keep going till 10 times unless you manually break it
  
#2) not recommended but if you want program to run no matter what
pyautogui.FALSESAFE = False

#3) if task is running too fast?
#per action (per function) delay 1 seconds:
pyautogui.PAUSE = 1

#so in usage, it can be outside of the loo:
pyautogui.PAUSE = 1
for i in range(1,10):
  pyautogui.move(100,100)

    
