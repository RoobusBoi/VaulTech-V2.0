from tkinter import *

#Driver code of all the buttons linking to other homes

##Password Generator Button
def btn_clicked0():
    print("Button0 Clicked")

##VPN Button
def btn_clicked1():
    print("Button1 Clicked")

##Website Checker Button
def btn_clicked2():
    print("Button2 Clicked")

##Privacy Checker Button
def btn_clicked3():
    print("Button3 Clicked")

##Website Blocker Button
def btn_clicked4():
    print("Button4 Clicked")

##Summon VaulT Button
def btn_clicked5():
    print("Button5 Clicked")

##About and Help Button
def btn_clicked6():
    print("Button6 Clicked")

#Code of the GUI
home = Tk()
home.geometry("906x505")
home.configure(bg = "#ffffff")
home.title("Homepage")

canvas = Canvas(home,bg = "#ffffff",height = 505,width = 906,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(453.0, 258.0,image=background_img)

##Password Generator tool button
img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0,borderwidth = 0,highlightthickness = 0,command = btn_clicked0,relief = "flat")
b0.place(x = 0, y = 68,width = 319,height = 57)

##VPN button
img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1,borderwidth = 0,highlightthickness = 0,command = btn_clicked1,relief = "flat")
b1.place(x = 0, y = 140,width = 319,height = 54)

##Website authenticity button
img2 = PhotoImage(file = f"img2.png")
b2 = Button(image = img2,borderwidth = 0,highlightthickness = 0,command = btn_clicked2,relief = "flat")
b2.place(x = 0, y = 208,width = 319,height = 56)

##Data privacy checker button
img3 = PhotoImage(file = f"img3.png")
b3 = Button(image = img3,borderwidth = 0,highlightthickness = 0,command = btn_clicked3,relief = "flat")
b3.place(x = 0, y = 282,width = 319,height = 54)

##Website blocker button
img4 = PhotoImage(file = f"img4.png")
b4 = Button(image = img4,borderwidth = 0,highlightthickness = 0,command = btn_clicked4,relief = "flat")
b4.place(x = 0, y = 356,width = 319,height = 54)

##Summon VaulT button
img5 = PhotoImage(file = f"img5.png")
b5 = Button(image = img5,borderwidth = 0,highlightthickness = 0,command = btn_clicked5,relief = "flat")
b5.place(x = 0, y = 425,width = 319,height = 54)

##About and Help button
img6 = PhotoImage(file = f"img6.png")
b6 = Button(image = img6,borderwidth = 0,highlightthickness = 0,command = btn_clicked6,relief = "flat")
b6.place(x = 347, y = 245,width = 241,height = 53)

home.resizable(False, False)
home.mainloop()