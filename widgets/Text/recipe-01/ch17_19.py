# ch17_19.py 
from tkinter import * 
from tkinter import messagebox
def cutJob():                            # Cut方法
    print("剪切操作执行中...")
    text.event_generate("<<Cut>>")
def copyJob():
    print("复制操作执行中...")
    text.event_generate("<<Copy>>")
def pasteJob():
    print("粘贴操作执行中...")
    text.event_generate("<<Paste>>")
def showPopupMenu(event):
    print("显示弹出菜单...")
    popupmenu.post(event.x_root,event.y_root)

root = Tk() 
root.title("ch17_19") 
root.geometry("300x180") 

popupmenu = Menu(root,tearoff=False)
# 在弹出菜单内建立三个命令列表
popupmenu.add_command(label="Cut",command=cutJob)
popupmenu.add_command(label="Copy",command=copyJob)
popupmenu.add_command(label="Paste",command=pasteJob)
# 单击鼠标右键绑定显示弹出菜单
root.bind("<Button-3>",showPopupMenu)

# 建立Text 
text = Text(root) 
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.insert(END,"Five Hundred Miles\n")           # 插入时同时设置Tag
text.insert(END,"If you miss the rain I'm on,\n")
text.insert(END,"You will know that I am gone.\n")
text.insert(END,"You can hear the whistle blow\n")
text.insert(END,"A hundred miles,\n")

root.mainloop() 

