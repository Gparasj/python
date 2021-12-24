from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

win=Tk()
win.title("Notepad")
win.geometry("500x500")

TextArea=scrolledtext.ScrolledText(win,font="lucida 13")
TextArea.pack(expand=True,fill=BOTH)
file=None

menubar=Menu(win)
win.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)
editmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)

def newfile():
    global file
    win.title("Untitled-Notepad")
    TextArea.delete(1.0,END)

def open():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("Text Doucments","*.txt")])
    if file=="":
        file=None
    else:
        win.title(os.path.basename(file)+"-Notepad")
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            win.title(os.path.basename(file)+ "-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def exitFile():
    win.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<paste>>"))

filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=open)
filemenu.add_command(label="Save",command=savefile)

filemenu.add_separator()

editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)

win.mainloop()


        
