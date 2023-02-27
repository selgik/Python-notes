#note_window_w_button.py
#credit: Youtube(Code your dreams: 53 tkinter) 
#flow: (1) user clicks a button (2) random quotes will be generated 


#1. PREPARE LIBRARIES
from tkinter import *
import random


#2. CREATE WINDOW
window = Tk()
window.title("Today's Quote Generator")
window.resizable(False, False)  #width/height of window box be fixed. User won't be able to adjust them


#3. EDIT WINDOW
canvas = Canvas(window, width=500, height=300, bg="pink") #assign size and background colour
canvas.pack()


#4. PREPARE TEXT
quotes = ["The greatest glory in living lies not in never falling, but in rising every time we fall",\
          "The way to get started is to quit talking and begin doing",\
          "Tell me and I forget. Teach me and I remember. Involve me and I learn"]
author = ["Nelson Mandela", "Walt Disney", "Benjamin Franklin"]


#5. ADD TEXT TO CANVAS
upper_T = canvas.create_text(250, 100, text = "Today's Quote", fill="red",\ 
                   font =("verdana", 20, "bold"), width=400, anchor="center") 
                          #thanks to width and anchor argument, texts(quotes variable) will be wrapped

bottom_T = canvas.create_text(250, 200, text = "", fill="gray",\
                   font =("verdana", 20, "bold"))


#6. PREPARE FUNCTION TO LINK TO THE BUTTON 
def click_btn():
    random_quote=random.randint(0,2)
    canvas.itemconfig(upper_T, text=quotes[random_quote])
    canvas.itemconfig(bottom_T, text=author[random_quote])
    
    
#7. CREATE BUTTON
button = Button(window, text="Click Me!", font =("gray", 20, "bold"),
                bg="pink", command=click_btn)
button.place(x=200, y=250)

  
