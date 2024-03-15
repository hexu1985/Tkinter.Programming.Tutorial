# ch17_4.py 
from tkinter import * 

root = Tk()
root.title("ch17_4")

yscrollbar = Scrollbar(root)
text = Text(root,height=5,width=30)
yscrollbar.pack(side=RIGHT,fill=Y)
text.pack() 
yscrollbar.config(command=text.yview)
text.config(yscrollcommand=yscrollbar.set)

myString = \
"""Python是一种跨平台的计算机程序设计语言。
是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。
最初被设计用于编写自动化脚本(shell)，随着版本的不断更新和语言新功能的添加，
越多被用于独立的、大型项目的开发。"""
text.insert(END,myString)

root.mainloop()

