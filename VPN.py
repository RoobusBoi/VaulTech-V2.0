from tkinter import *

#VPN connection commence
def btn_clicked():
    print("Button Clicked")

#Code of the GUI
vpn = Tk()
vpn.geometry("906x505")
vpn.configure(bg = "#ffffff")
vpn.title("Virtual Private Network")

canvas = Canvas(vpn, bg = "#ffffff", height = 505, width = 906, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(453.0, 258.0, image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(318.5, 238.0, image = entry0_img)
entry0 = Entry(bd = 0, bg = "#fff4f4",highlightthickness = 0)
entry0.place(x = 165, y = 215,width = 310,height = 45)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b0.place(x = 159, y = 393, width = 319, height = 54)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked,relief = "flat")
b1.place(x = 0, y = 460, width = 76,height = 37)

vpn.resizable(False, False)
vpn.mainloop()
