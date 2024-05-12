from tkinter import *
import pandas as pd
window = Tk()

window.geometry("400x400")

df=pd.read_csv("data2.csv")
df=df.dropna()
s=0
for x in df["Calories"]:
    s=s+x

txt=Label(window,text="Sum = "+str(s))
txt.grid(column=0,row=0)

window.title("Hello world")
window.mainloop()