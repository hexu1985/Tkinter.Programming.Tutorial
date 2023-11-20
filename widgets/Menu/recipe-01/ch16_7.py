# ch16_7.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","新建文档")

root = Tk()
root.title("ch16_7")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File",
                    command=newFile,accelerator="Ctrl+N")
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)

root.config(menu=menubar)    # 显示菜单对象
root.bind("<Control-N>",lambda event:messagebox.showinfo("New File","新建文档"))

root.mainloop()

