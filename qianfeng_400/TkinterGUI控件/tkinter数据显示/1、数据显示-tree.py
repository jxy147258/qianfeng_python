import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# 表格Tree
tree = ttk.Treeview(win)
tree.pack()

# 定义列
tree["columns"] = ["姓名","年龄","身高","体重"]
# 设置列宽度
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)
# 设置表头显示名称
tree.heading("姓名",text="姓名")
tree.heading("年龄",text="年龄")
tree.heading("身高",text="身高")
tree.heading("体重",text="体重")
# 添加数据
tree.insert("",0,text = "第一行",values=("张三","19","190","90"))
tree.insert("",1,text = "第二行",values=("张三", "19","190","90"))
tree.insert("",2,text = "第三行",values=("张三","19","190","90"))


win.mainloop()