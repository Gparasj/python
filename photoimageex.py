from tkinter import *
from tkinter import PhotoImage

win=Tk()
win.title("Image")
win.geometry("500x500")

bm=PhotoImage(file="C:\Users\visha\Desktop\img19.jpg")

btn=Button(win,text="image",image=bm)
btn.pack()

win.mainloop()
