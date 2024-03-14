# ch16_3.py
from tkinter import *
from tkinter import messagebox

def newFile():
    messagebox.showinfo("New File","新建文档")

root = Tk()
root.title("ch16_3")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=filemenu)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File",command=newFile)
filemenu.add_command(label="Exit!",command=root.destroy)
root.config(menu=menubar)    # 显示菜单对象

root.mainloop()

