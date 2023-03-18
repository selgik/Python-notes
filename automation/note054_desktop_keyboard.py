#note054_desktop_keyboard.py
import pyautogui


########## 1. WRITE
#only works with alphabet and number
pyautogui.write("12345")
pyautogui.write("I am a boy", interval = 1)   #takes 1 sec to write each character
pyautogui.write("Test", interval = 0.25)      #takes 0.25 sec to write each character


########## 2. USING KYEBOARD KYES
#keyboard attribute: https://automatetheboringstuff.com/2e/chapter20/#calibre_link-1634 (Table 20-1)

#1) direction keys
#below will write test -> move cursor to the leftx2 -> rightx1 -> write la -> enter. 
pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "right", "l", "a", "enter"], interval=0.25) 

#2) special keys
#2-1) result for below is dollar shign: shift+4 = $
pyautogui.keyDown("shift")  
pyautogui.press("4")
pyautogui.keyUp("shift")

#2-2) result for below is selecting all (CTRL+A)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")
pyaugogui.keyUp("ctrl")

#3) above codes however are too long, let's shorten them
### also, use it when you need to press multiple keys at the same time. 2-2 won't work for simultaneous press.
pyautogui.hotkey("ctrl", "a")
pyautogui.hotkey("ctrl", "alt", "shift", "a")
#flow: keydown ctrl>alt>shift>a --> keyup a>shift>alt>ctrl


########## 3. HOW TO TYPE KOREAN? (OR OTHER NON-ALPHABETIC LANGUAGE?)
#install pyperclip on the terminal: pip install pyperclip

#1) how to use:
import pyperclip
pyperclip.copy("나는 짱이다")      #copy the sentence to the clipboard
pyautogui.hotkey("ctrl", "v")   #paste the copied sentence back

#2) create function if too troublesome:
def type_kor(text):
  pyperclip.copy(text)
  pyautogui.hotkey("ctrl", "v")
  
type_kor("나는 파이썬 천재이시다")
type_kor("나는 게으름 대마왕이시다")
type_kor("모두 행복해 지십시오")


########## 4. SHUT DOWN RPA
#Apart from moving mouse to the corner, force shut down RPA with:
#windows: ctrl + alt + del
#mac    : cmd + shift + option + q

    
