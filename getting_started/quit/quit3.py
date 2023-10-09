import sys
from tkinter import *

root = Tk()
widget = Button(root, 
        text='Hello event world', 
        command=(lambda: print("Hello lambda world") or sys.exit()))
widget.pack()
root.mainloop()
