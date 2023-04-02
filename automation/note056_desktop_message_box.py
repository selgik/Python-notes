#note056_desktop_alert.py
import pyautogui


########## 1. COUNTDOWN
#below will type 3 2 1 and then process the code
print("RPA will begin soon")
pyautogui.countown(3)
print("Starting RPA")


########## 2. MESSAGE BOX FUNCTIONS
#refer doc: https://pyautogui.readthedocs.io/en/latest/msgbox.html#the-alert-function

#1) OK button 
#below will show an alert (pop-up) with title "WARNING"
pyautogui.alert("RPA has failed", "WARNING") 

#2) OK / CANCEL button
#below will print the result (Ok or Cancel), and depending on the result, different action can be built
result = pyautogui.confirm("Are you sure to continue?", "confirm")
print(result)

#3) TEXT INPUT button with OK/CANCEL
result = pyautogui.prompt("enter fil'es name", "enter")
print(result)

#4) PASSWORD button with OK/CANCEL 
#when user types, it will show as *** but real character will show up on termial as print() is used
result = pyautogui.password("Enter your password")
print(result)

    
