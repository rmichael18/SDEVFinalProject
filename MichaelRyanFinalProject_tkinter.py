'''
Ryan Michael Final TKinter Program
Date Modified: 5/10/23
'''
import sys
import os
from tkinter import * 
from tkinter.ttk import *
# creating tkinter window
root = Tk()
root.title("Running Python Script")
root.geometry('550x200')
# Adding widgets to the root window
Label(root, text = 'Dungeons & Dragons Character Generator', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)
  
# Creating a photoimage object to use image
def Roll():
    os.system('python DnD_CharacterGenerator.py')
photo = PhotoImage(file = r"C:\Users\r_a_m\OneDrive\Documents\College Assignments\SDEV140\D20.png")
  
# Resizing image to fit on button
photoimage = photo.subsample(3, 3)
  
# sets image and button for character roller. SHOULD run my character generator but cannot get the
# program to work as intended
Button(root, text = 'Roll Character!', image = photoimage, command=Roll,
                    compound = LEFT).pack(side = TOP)
  
mainloop()
