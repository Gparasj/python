from tkinter import *
from tkinter import messagebox
import mysql.connector

win=Tk()
win.title("Login")
win.geometry("500x500")

my=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="paras"
    )
mycursor=my.cursor()

tv1=StringVar()
tv2=StringVar()

def btn_click():
    t1=(str(tv1.get()))
    t2=(str(tv2.get()))
    h=(t1,t2)
    y=("select * from login where name=%s and pass=%s")
    mycursor.execute(y,h)

    if mycursor==True:
        top=Tk()
        top.title("daseboard")
        top.geometry("500x500")
        top.configure(backgroung="skyblue")
    else:
        messagebox.showerror("error","Login Fail")
        win.quit()

l1=Label(win,text="Username")
t1=Entry(win,textvariable=tv1)

l2=Label(win,text="Password")
t2=Entry(win,textvariable=tv2)

btn=Button(win,text="Login",command=btn_click)
btn.grid(column=1,row=3)
l1.grid(column=1,row=1)
t1.grid(column=2,row=1)
l2.grid(column=1,row=2)
t2.grid(column=2,row=2)

win.mainloop()
