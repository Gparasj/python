from tkinter import *

win=Tk()
win.title("spinbox example")
win.geometry("500x200")

v=IntVar()
s_box=Spinbox(win,from_=11,to=20,textvariable=v)
Label(win,textvariable=v).pack()
s_box.pack()

win.mainloop()