from tkinter import *

root = Tk()
widget = Button(root, text='Hello widget world', command=root.quit)
widget.pack()
root.mainloop()
