# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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


