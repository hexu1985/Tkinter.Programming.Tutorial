import tkinter as tk
import turtle

# 创建主窗口
root = tk.Tk()
# 设置窗口标题
root.title("小海龟游戏")
# 设置窗口大小
root.geometry("600x400")

canvas = tk.Canvas(root, width=525, height=300, bg='white')   # 0,0 is top left corner
canvas.pack(expand=tk.YES, fill=tk.BOTH)                   # increases down, right

# 创建小海龟
t = turtle.RawTurtle(canvas)

# 设置画笔颜色
t.pencolor("red")
# 设置画笔宽度
t.pensize(4)
# 设置填充颜色
t.fillcolor("yellow")
# 开始填充
t.begin_fill()
# 绘制海龟的头部
t.circle(50)

# 绘制海龟的身体
for i in range(3):
    t.forward(100)
    t.left(120)

# 结束填充
t.end_fill()

# 创建控制面板
control_panel = tk.Frame(root, padx=10, pady=10)
control_panel.pack(side='right', fill='y')

# 创建控制按钮，并添加到控制面板中
up_btn = tk.Button(control_panel, text="向上运动")
up_btn.pack(side='left')

down_btn = tk.Button(control_panel, text="向下运动")
down_btn.pack(side='left')

left_btn = tk.Button(control_panel, text="向左运动")
left_btn.pack(side='left')

right_btn = tk.Button(control_panel, text="向右运动")
right_btn.pack(side='left')

# 定义控制函数
def move_up(event):
    t.setheading(90)
    t.fd(10)

def move_down(event):
    t.setheading(270)
    t.fd(10)

def move_left(event):
    t.setheading(180)
    t.fd(10)

def move_right(event):
    t.setheading(0)
    t.fd(10)

# 绑定事件
up_btn.bind('<Button-1>', move_up)
down_btn.bind('<Button-1>', move_down)
left_btn.bind('<Button-1>', move_left)
right_btn.bind('<Button-1>', move_right)


root.mainloop()
