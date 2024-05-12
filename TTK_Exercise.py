from tkinter import *
from tkinter.ttk import *

window=Tk()
window.title("Hello World")
window.geometry("400x400")

txt=Label(window,text="",font=("Arial Bold",50))


dropbox=Combobox(window)
dropbox["values"]=[1,2,3,4,5]
dropbox.current(0)

def click():
    txt.configure(text=dropbox.get())
bt=Button(window,text="Click Me",command=click)

bt.grid(column=0,row=1)
txt.grid(column=0,row=2)
dropbox.grid(column=0,row=0)
window.mainloop()