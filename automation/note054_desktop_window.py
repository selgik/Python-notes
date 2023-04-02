#note054_desktop_window.py
#window functions will only work in Window, not in MacOS

import pyautogui


########## 1. getActiveWindow()
fw = pyautogui.getActiveWindow()    #get currently active window (ex. VSCODE)
print(fw.title)                     #get title of window
print(fw.size)                      #get size of window
print(fw.left, fw.top, fw.right, fw.bottom)   #get coordinate of window
pyautogui.click(fw.left+25, fw.top+20)        #based on coordinate, move and click
                                              #especially useful when we have multiple windows(app) opened
  
########## 2. getAllWindows()
for w in pyautogui.getAllWindows():
  print(w)                          #result: every active windows' coordinates and title will be printed 
 

########## 3. getWindowsWithTitle()
for w2 in pyautogui.getWindowsWithTitle("paint"):
  print(w2)                          #result: window title matching "paint" will be printed
  
w3 = pyautogui.getWindowsWithTitle("paint")[0]
print(w3)                         #result: first item (on the list of) window where title matches "paint" will be printed
  
  
########## 4. ACTIVATE / MAXIMIZE / MINIMIZE / RESTORE / CLOSE
if w3.isActive == "False":        #activate window if not activated yet
  w3.activate 

if w3.isMaximized == "False":     #maximize window if not maximized yet
  w3.maximize()
 
if w3.isMinimized == "False":    #maximize window if not minimized yet
  w3.minimize()
  
w3.restore()                     #restore to original status  
w3.close()                       #close the window (system may ask whether to save or not)

  
