import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="grey")

def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

Label(win, text= "Enter Your URL Link", font="impact 17 bold", bg="black",fg="white").pack(fill="x")

entry1 = Entry(win,font="10",bd=3,width=40)
entry1.pack(pady=20)

Button(win, text="Click Me",font="impact 12 bold", bg="blue",fg="white", width="12",command=short).pack()

entry2 = Entry(win,font="imapact 16 bold", bg="grey", width=22, bd=0)
entry2.pack(pady=25)



mainloop()


