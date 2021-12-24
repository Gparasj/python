from tkinter import *

win=Tk()
win.title("Scrollbar")
s=Scrollbar(win)
s.pack(side=RIGHT)

l=Listbox(win,yscrollcommand=s.set)

for i in range(50):
    l.insert(i,"SSSDIIT"+str(i))

l.pack(side=RIGHT,fill=BOTH)
s.config(command=l.yview)

win.mainloop()
