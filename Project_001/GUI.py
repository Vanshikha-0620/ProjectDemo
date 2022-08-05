#opencv-contrib-python
#opencv-python
#numpy
#cvzone
#Pillow-PIL
#Pillow

from tkinter import *
from PIL import  Image, ImageTk
import os
import threading
#import customtkinter

def __ma__():
    filename = 'main.py'
    os.system(filename)
    os.system('notepad'+filename)

def __ve__():
    filename = 'vehicle.py'
    os.system(filename)
    os.system('notepad'+filename)

def __ex__():
    root.destroy()

root = Tk()

root.geometry('900x460')#+200+50
root.resizable(FALSE, FALSE)
title = Label(root, text="Car Parking + Vehicle Counter", font=('Times New Roman', 30),
              bg='#0a064f', fg='white')
title.place(x=0, y=0, relwidth=1)
frm = Frame(root, bd=0, relief=RIDGE, bg='white')
#frm.place(x=55,y=70, width=790, height=260)
#root.update()

load=Image.open("C:/Users/Sync/Desktop/PythonImg/PC2.jpg")
render = ImageTk.PhotoImage(load)
img = Label( image = render)
img.place(x=0, y=50, width=450, height=400)

load1=Image.open("C:/Users/Sync/Desktop/PythonImg/VD4.jpg")
render1 = ImageTk.PhotoImage(load1)
img1 = Label( image = render1)
img1.place(x=450, y=50, width=450, height=400)

#btn = Button(root, text='Parking_Detection', font=('Times New Roman', 15), bg='#326fa8', bd=10, fg='white', command=__ma__)
btn = Button(master=root, text='Parking_Detection', font=('Times New Roman', 15), bg='#326fa8', bd=10, fg='white', command = threading.Thread(target=__ma__).start)
btn.place(x=70,y=400)


#btn2 = Button(root, text='Vehicle_Detection',font=('Times New Roman', 15), bg='#326fa8', bd=10, fg='white', command=__ve__)
btn2 = Button(root, text='Vehicle_Detection',font=('Times New Roman', 15), bg='#326fa8', bd=10, fg='white', command = threading.Thread(target=__ve__).start)
btn2.place(x=600,y=400)


btn3 = Button(root, text="Exit", font=('Times New Roman', 15), bg='#326fa8', bd=10, fg='white', command =__ex__)
btn3.place(x=420,y=400)


root.mainloop()

