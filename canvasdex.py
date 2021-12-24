from tkinter import *

win=Tk()
win.title("canvas")
win.geometry("500x500")

ca=Canvas(win,width=500,height=500,bg="red")
ca.pack()

ca.create_line(10,10,100,10)
coord=10,50,240,210
arc=ca.create_arc(coord,start=10,extent=150,fill="blue")

win.mainloop()
