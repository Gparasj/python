import tkinter as tk


win=tk.Tk()
win.title("Scale")
win.geometry("500x200")

def btn_color(v):
    color_c="#%02x%02x%02x"%(s1.get(),s2.get(),s3.get())
    btn1.config(bg=color_c)
    btn1.config(text=color_c)
font1=("Time",18,"normal")    
s1=tk.Scale(win,from_=0,to=255,showvalue=1,resolution=1,command=btn_color,bg="red",orient="horizontal")
s1.grid(column=0,row=0,padx=5,pady=10)

s2=tk.Scale(win,from_=0,to=255,showvalue=1,resolution=1,command=btn_color,bg="green",orient="horizontal")
s2.grid(column=0,row=1,pady=10)

s3=tk.Scale(win,from_=0,to=255,showvalue=1,resolution=1,command=btn_color,bg="blue",orient="horizontal")
s3.grid(column=0,row=2,pady=10)

btn1=tk.Button(win,text="Color",font=font1,width=8)
btn1.grid(row=1,column=1,padx=7)
win.mainloop()
