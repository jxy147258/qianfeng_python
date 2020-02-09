from tkinter import *

root = Tk()
text = StringVar()
text.set('unselect')  # 给label设置初始值

status = IntVar()


def change():  # 选中事件
    if status.get() == 1:  # 判断是否被选中
        text.set('selected')
    else:
        text.set('unselect')


cb = Checkbutton(root, variable=status, command=change).pack()  # 给Checkbutton添加选中事件
lb = Label(root, textvariable=text).pack()
root.mainloop()