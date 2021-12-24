import tkinter as tk

win=tk.Tk()
win.title("Change Item")
win.geometry("500x500")
l1=tk.Listbox(win,height='5')
l2=tk.Listbox(win,height='5')
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)

mylist=['1','2','3','4','5']

for item in mylist:
    l1.insert(item)

def delete():
    l1.delete(ANCHOR)

def select():
    l2.insert(l1.get(ANCHOR))

b1=tk.Button(win,text="delete",command=delete)
b2=tk.Button(win,text="select",command=select)
b1.grid(row=0,column=1)
b2.grid(row=1,column=1)

lbl=tk.Label(win,text="My_label")
lbl.grid(row=2,column=1)

win.mainloop()

