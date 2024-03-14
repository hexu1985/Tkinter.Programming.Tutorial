# ch16_6.py
from tkinter import *
from tkinter import messagebox
def newFile():
    messagebox.showinfo("New File","新建文档")
def openFile():
    messagebox.showinfo("New File","打开文档")
def saveFile():
    messagebox.showinfo("New File","保存文档")
def saveAsFile():
    messagebox.showinfo("New File","另存为")
def aboutMe():
    messagebox.showinfo("New File","洪锦魁著")

root = Tk()
root.title("ch16_6")
root.geometry("300x180")

menubar = Menu(root)      # 建立最上层菜单
# 建立菜单类别对象,并将此菜单类别命名为File
filemenu = Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu,underline=0)
# 在File菜单内建立菜单列表
filemenu.add_command(label="New File",command=newFile,underline=0)
filemenu.add_command(label="Open File",command=openFile,underline=0)
filemenu.add_separator()
filemenu.add_command(label="Save",command=saveFile,underline=0)
# filemenu.add_separator()########################
filemenu.add_command(label="Save As",command=saveAsFile,underline=5)
filemenu.add_separator()
filemenu.add_command(label="Exit!",command=root.destroy,underline=0)
# 建立菜单类别对象,并将此菜单类别命名为Help
helpmenu = Menu(menubar)
menubar.add_cascade(label="Help",menu=helpmenu,underline=0)
# 在Help菜单内建立菜单列表
helpmenu.add_command(label="About me",command=aboutMe,underline=1)

root.config(menu=menubar)    # 显示菜单对象

root.mainloop()

