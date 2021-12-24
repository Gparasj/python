import tkinter as tk
from tkinter import messagebox
import mysql.connector


win=tk.Tk()
win.title("Insert")
win.geometry("500x500")

tv1=tk.StringVar()
tv2=tk.StringVar()
tv3=tk.StringVar()

mydb=mysql.connector.connect(
   host="localhost",
   username="root",
   password="",
   database="paras")
mycursor=mydb.cursor()

def btn_click():
    insert="insert into stud(id,name,city)values(%s,%s,%s)"
    id=t1.get()
    name=t2.get()
    city=t3.get()

    value=(id,name,city)
    mycursor.execute(insert,value)
    mydb.commit()
    messagebox.askokcancel("data","Insert Record")

def btn_search():
    id=t1.get()
    id=""
    select="select id from stud where id='%s'"%(id)
    mycursor.execute(select)
    r1=mycursor.fetchall()
    for i in r1:
        id=i[0]
def btn_delete():
    pass
def btn_update():
    pass
   

l1=tk.Label(win,text="id")
t1=tk.Entry(win,textvariable=tv1)

l2=tk.Label(win,text="Name")
t2=tk.Entry(win,textvariable=tv2)

l3=tk.Label(win,text="city")
t3=tk.Entry(win,textvariable=tv3)

btn=tk.Button(win,text="Insert",command=btn_click)
btn1=tk.Button(win,text="search",command=btn_search)
btn2=tk.Button(win,text="Delete",command=btn_delete)
btn3=tk.Button(win,text="Update",command=btn_update)

btn.grid(column=1,row=4)
btn1.grid(column=2,row=4)
l1.grid(column=1,row=1)
t1.grid(column=2,row=1)

l2.grid(column=1,row=2)
t2.grid(column=2,row=2)

l3.grid(column=1,row=3)
t3.grid(column=2,row=3)

win.mainloop()
