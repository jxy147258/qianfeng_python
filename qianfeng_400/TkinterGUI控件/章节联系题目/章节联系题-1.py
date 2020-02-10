import tkinter
from tkinter import ttk
import os
win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


tree = ttk.Treeview(win)
tree.pack()

# 添加一级树枝
# 空字符串的含义是本级树枝的上一级树枝为空，如果有上一级就填入上一级名称
i = 0
for item in os.listdir():
    treeF1 = tree.insert("", i,item, text=item, values=item)
    print(i)
    i += 1
# 如何得到treeF2，
# # 添加二级树枝
treeF1_1 = tree.insert(treeF1, 0, "北京", text="中国-北京", values="F1-1")
treeF1_2 = tree.insert(treeF1, 1, "天津", text="中国-天津", values=("F1-2"))
treeF1_3 = tree.insert(treeF1, 2, "上海", text="中国-上海", values=("F1-3"))
# # 添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"北京朝阳区",text="北京-朝阳区",values=("F1-1-1"))
treeF1_1_2 = tree.insert(treeF1_1,1,"北京海淀区",text="北京-海淀区",values=("F1-1-2"))
treeF1_1_3 = tree.insert(treeF1_1,2,"北京昌平区",text="北京-昌平区",values=("F1-1-3"))

win.mainloop()