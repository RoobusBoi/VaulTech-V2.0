from tkinter import *
import webbrowser

#Code for opening the online database
def btn_clicked():
     webbrowser.open("https://www.mywot.com")


#Code for the GUI
webchck = Tk()
webchck.geometry("906x505")
webchck.configure(bg = "#ffffff")
webchck.title("Website safety checker")

canvas = Canvas(webchck, bg = "#ffffff", height = 505, width = 906, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(453.0, 258.0,image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place(x = 1, y = 455, width = 76, height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 174, y = 388, width = 319, height = 54)

webchck.resizable(False, False)
webchck.mainloop()