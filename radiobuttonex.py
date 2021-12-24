import tkinter as tk 
from tkinter import messagebox

win=tk.Tk()
win.title("RadioButton")
win.geometry("500x200")
rv= tk.IntVar()
def btn_click():
    v=rv.get()
    if(v==1):
       msg=messagebox.showinfo(message="Radio1")
    elif(v==2):
        Messagebox.showinfo(message="Radio2")
rd1=tk.Radiobutton(win,text="Male",variable=rv,value=1)
rd2=tk.Radiobutton(win,text="Female",variable=rv,value=2)

btn=tk.Button(win,text="Submit",command=btn_click)
rd1.pack()
rd2.pack()
btn.pack()
win.mainloop()
