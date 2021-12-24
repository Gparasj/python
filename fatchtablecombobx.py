import tkinter as tk
from tkinter import ttk
import mysql.connector

win=tk.Tk()
win.title("combobox")
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

n=tk.StringVar()

table=ttk.Combobox(win,textvariable=n)

table['value']=result
                
                
table.pack()
table.current()
win.mainloop()
