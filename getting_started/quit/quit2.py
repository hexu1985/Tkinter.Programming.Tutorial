import sys
from tkinter import *

def quit():
    print('Hello, I must be going...')
    sys.exit()

root = Tk()
widget = Button(root, text='Hello event world', command=quit)
widget.pack()
root.mainloop()

