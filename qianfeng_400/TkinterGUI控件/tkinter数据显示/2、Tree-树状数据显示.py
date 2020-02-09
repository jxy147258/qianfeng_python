import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


tree = ttk.Treeview(win)
tree.pack()

# 设置一级树
treeF1 = tree.insert("",0,"中国",text="中国CHI",values=("F1"))
treeF1 = tree.insert("",1,"美国",text="美国USA",values=("F1"))
treeF1 = tree.insert("",2,"英国",text="英国BRI",values=("F1"))
treeF1 = tree.insert("",3,"波兰",text="波兰POL",values=("F1"))


win.mainloop()