from tkinter import *
import string
import random
import numpy as np
import pyperclip


#Code for password generator
password_chars = string.ascii_letters + string.digits + string.punctuation
def password_generator():
    entry1.delete(0)
    length = int(entry0.get())
    password = "".join([random.choice(password_chars) for _ in range(length)])
    entry1.insert(0, password)
    pyperclip.copy(password)

def btn_clicked():
    print("Going Back to Homepage")

#Code for GUI
pswdgenerator = Tk()
pswdgenerator.geometry("906x505")
pswdgenerator.configure(bg = "#ffffff")
pswdgenerator.title("Password generator")

canvas = Canvas(pswdgenerator,bg = "#ffffff",height = 505,width = 906,bd = 0,highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(453.0, 258.0,image=background_img)

#Password length input box
entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(320.0, 178.0, image = entry0_img)
entry0 = Entry(bd = 0,bg = "#fff4f4",highlightthickness = 0)
entry0.place(x = 68, y = 160,width = 500,height = 30)
entry0.insert(0, "Enter the number of characters you would like in your password.")
entry0.focus()

#Password output box
entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(320.0, 294.0,image = entry1_img)
entry1 = Entry(bd = 0,bg = "#fff4f4",highlightthickness = 0)
entry1.place(x = 69, y = 217,width = 490,height = 100)

#Generate and Copy Button
img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = password_generator,relief = "flat")
b0.place(x = 165, y = 388,width = 319,height = 54)

#Home Button
img1 = PhotoImage(file = f"img1.png")
b1 = Button( image = img1,borderwidth = 0,highlightthickness = 0,command = btn_clicked,relief = "flat")
b1.place(x = 0, y = 458, width = 76,height = 37)

pswdgenerator.resizable(False, False)
pswdgenerator.mainloop()