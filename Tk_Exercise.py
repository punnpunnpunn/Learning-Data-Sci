from tkinter import *

window = Tk()

window.geometry("400x400")

txt=Label(window,text="Hello",font=("Arial Bold",50))
txt2=Label(window,text="World",font=("Arial",50))

tb=Entry(window,width=20)

def click():
    txt.configure(text="Button was clicked")
    txt2.configure(text=tb.get())

bt=Button(window,text="Click Me",bg="hot pink",command=click)

bt.grid(column=1,row=0)
tb.grid(column=1,row=1)
txt.grid(column=0,row=0)
txt2.grid(column=0,row=1)
window.title("Hello world")
window.mainloop()