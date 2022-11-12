from tkinter import *
import webbrowser

#Code to open the online database
def btn_clicked():
    webbrowser.open("https://haveibeenpwned.com")

#Code of the GUI
privchck = Tk()
privchck.geometry("906x505")
privchck.configure(bg = "#ffffff")
privchck.title("Data privacy checker")

canvas = Canvas(privchck,bg = "#ffffff",height = 505, width = 906, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image( 453.0, 258.0, image=background_img)
img0 = PhotoImage(file = f"img0.png")

b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place( x = 0, y = 452, width = 76, height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 162, y = 389, width = 319,height = 54)

privchck.resizable(False, False)
privchck.mainloop()