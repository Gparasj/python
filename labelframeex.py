from tkinter import *

win=Tk()
win.title("Label frame")
win.geometry("500x500")

fm=LabelFrame(win,text="Personal information",padx=10,pady=10)

fm.pack(padx=20,pady=20,fill=BOTH)

win.mainloop()
