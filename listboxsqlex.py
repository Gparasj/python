import tkinter as tk
from tkinter import messagebox
import mysql.connector

win=tk.Tk()
win.title("Listbox")
win.geometry("500x500")

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="paras"
    )
mycursor=mydb.cursor()
mycursor.execute("SHOW TABLES")
result=mycursor.fetchall()

l1=tk.Listbox(win,height=10,width=15,bg="grey",activestyle="dotbox")
for i in range(len(result)):
    l1.insert(i,result)
                
                
l1.pack()

win.mainloop()
