# ch17_8.py 
from tkinter import * 
from tkinter.font import Font

def familyChanged(event):             # font family更新
    f=Font(family=familyVar.get())    # 取得新的fong family
    text.configure(font=f)            # 更新text的font family
def weightChanged(event):             # weight family更新
    f=Font(weight=weightVar.get())    # 取得新的fong weight
    text.configure(font=f)            # 更新text的font weight

root = Tk()
root.title("ch17_8")
root.geometry("300x180")

# 建立工具栏
toolbar = Frame(root,relief=RAISED,borderwidth=1)
toolbar.pack(side=TOP,fill=X,padx=2,pady=1)

# 建立font family OptionMenu
familyVar = StringVar()
familyFamily = ("Arial","Times","Courier")
familyVar.set(familyFamily[0])
family = OptionMenu(toolbar,familyVar,*familyFamily,command=familyChanged)
family.pack(side=LEFT,pady=2)

# 建立font weight OptionMenu
weightVar = StringVar()
weightFamily = ("normal","bold")
weightVar.set(weightFamily[0])
weight = OptionMenu(toolbar,weightVar,*weightFamily,command=weightChanged)
weight.pack(pady=3,side=LEFT)

# 建立Text
text = Text(root)
text.pack(fill=BOTH,expand=True,padx=3,pady=2)
text.focus_set()

root.mainloop()

