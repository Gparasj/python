from tkinter import *

win=Tk()
win.title("Calulator")
win.geometry("500x500")

def btn_click():
    global expression
    expression=expression + str(item)
    text.set(expression)

def btn_clear():
    global expression
    expression=""
    text.set("")

def btn_equal():
    global expression
    result=str(eval(expression))
    text.set(result)
expression=""

text=StringVar()
frame=Frame(win,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
frame.pack(side=TOP)
field=Entry(frame,font=('arial',18,'bold'),textvariable=text,width=50,bg="#eee",bd=0,justify=RIGHT)
field.grid(row=0,column=0)
field.pack(ipady=10)
btn_frame=Frame(win,width=312,height=272.5,bg="grey")
btn_frame.pack()
clear=Button(btn_frame,text="c",fg="black",width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_clear())
divide=Button(btn_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("/"))
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide.grid(row=0,column=3,padx=1,pady=1)

btn7=Button(btn_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(7))
btn8=Button(btn_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(8))
btn9=Button(btn_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(9))
multi=Button(btn_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("*"))
btn7.grid(row=1,column=0,padx=1,pady=1)
btn8.grid(row=1,column=1,padx=1,pady=1)
btn9.grid(row=1,column=2,padx=1,pady=1)
multi.grid(row=1,column=3,padx=1,pady=1)

btn6=Button(btn_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(6))
btn5=Button(btn_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(5))
btn4=Button(btn_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(4))
sub=Button(btn_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("-"))
btn6.grid(row=2,column=0,padx=1,pady=1)
btn5.grid(row=2,column=1,padx=1,pady=1)
btn4.grid(row=2,column=2,padx=1,pady=1)
sub.grid(row=2,column=3,padx=1,pady=1)


btn3=Button(btn_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(3))
btn2=Button(btn_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(2))
btn1=Button(btn_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(1))
add=Button(btn_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:btn_click("+"))
btn3.grid(row=3,column=0,padx=1,pady=1)
btn2.grid(row=3,column=1,padx=1,pady=1)
btn1.grid(row=3,column=2,padx=1,pady=1)
add.grid(row=3,column=3,padx=1,pady=1)


zero=Button(btn_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click(0))
point=Button(btn_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:btn_click("."))
zero.grid(row=4,column=0,columnspan=2,padx=1,pady=1)
point.grid(row=4,column=0,padx=2,pady=1)


