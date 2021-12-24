from tkinter import *

win=Tk()
win.title("Message")
win.geometry("500x500")

msg=Message(win,text="This is Message",width=3000,bg="blue",fg="yellow")
msg.pack()

win.mainloop()
