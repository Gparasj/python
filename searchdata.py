import tkinter as tk
import mysql.connector

win=tk.Tk()
win.title("search")
win.geometry("500x500")

tv1=tk.StringVar()


mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="paras"
    )
mycursor=mydb.cursor()

def btn_click():
    id=t1.get()
    
    se="select id from stud where id='id'"
    mycursor.execute(se)
    i=0
    for s in mycursor:
       for j in range(len(s)):
          e=tk.Entry(win,width=15,fg="blue")
          e.grid(row=i,column=j)
          e.insert(s[j])
    i=i+1
      
   

   
"""mycursor.execute("select * from stud ")
i=0
for s in mycursor:
    for j in range(len(s)):
        e=tk.Entry(win,width=15,fg="blue")
        e.grid(row=i,column=j)
        e.insert(s[j])
    i=i+1
"""
l1=tk.Label(win,text="id")
t1=tk.Entry(win,textvariable=tv1)

btn=tk.Button(win,text="Insert",command=btn_click)
l1.grid(column=1,row=1)
t1.grid(column=2,row=1)
btn.grid(column=1,row=2)


win.mainloop()
