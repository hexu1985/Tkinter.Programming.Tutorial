from tkinter import *

root = Tk()
root.option_readfile('optionDB')
root.title('OptionMenu')

var = StringVar()
var.set('Quantity Surveyor')
opt_menu = OptionMenu(root, var, 'Stockbroker', 'Quantity Surveyor', 'Church Warden', 'BRM')
opt_menu.pack(anchor=W, padx=20, pady=30)

root.mainloop()

