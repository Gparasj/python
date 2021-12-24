import tkinter as tk

win=tk.Tk()

Width=win.winfo_reqwidth()
Height=win.winfo_reqheight()
print("Width",Width,"height",Height)
      
Right=int(win.winfo_screenwidth()/2 - Width/2)
Down=int(win.winfo_screenheight()/2 - Height/2)

win.geometry("+{}+{}".format(Right,Down))
win.mainloop()
