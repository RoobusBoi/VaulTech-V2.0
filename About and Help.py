from tkinter import *

#Back to home button code
def btn_clicked():
    print("Button Clicked")

#Code for the GUI
aboutandhelp = Tk()
aboutandhelp.geometry("915x499")
aboutandhelp.configure(bg = "#ffffff")
aboutandhelp.title("About and Help")

canvas = Canvas(aboutandhelp, bg = "#ffffff", height = 499, width = 915, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image( 468.0, 252.5, image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place(x = 1, y = 461, width = 76,height = 37)

aboutandhelp.resizable(False, False)
aboutandhelp.mainloop()