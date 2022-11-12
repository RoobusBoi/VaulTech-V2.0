from tkinter import *

#Code for the website Blocker
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

def btn_clicked():
    website_lists = entry0.get(1.0,END)
    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

#Code of the GUI
webblock = Tk()
webblock.geometry("906x505")
webblock.configure(bg = "#ffffff")
webblock.title("Website")

canvas = Canvas(webblock, bg = "#ffffff", height = 505, width = 906, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(453.0, 258.0,image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0,command = btn_clicked, relief = "flat")
b0.place(x = 0, y = 457, width = 76,height = 37)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image( 312.0, 230.0, image = entry0_img)
entry0 = Text(bd = 0, bg = "#fff4f4", highlightthickness = 0, font = 'arial 12')
entry0.place(x = 62, y = 210, width = 500, height = 40)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = btn_clicked, relief = "flat")
b1.place(x = 167, y = 390,width = 319,height = 54)

webblock.resizable(False, False)
webblock.mainloop()