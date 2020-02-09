import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# 列表框，可以包含一个或者多个文本框
# 在listbox控件的小窗口显示一个字符串
listbox = tkinter.Listbox(win,
                          width = 100 ,
                          height = 10,
                          selectmode  = tkinter.BROWSE,

                          )

listbox.pack()
for item in ["good","cool","nice","handsome"]:
    # tkinter.END是从前往后
    listbox.insert(tkinter.END,item)
# ACTIVE，是不管现在有多少内容，都从头依次往后
listbox.insert(tkinter.ACTIVE,"COOL","GOOD")
listbox.insert(tkinter.END,["very good","very nice"])

# 删除
# listbox.delete(0,1) # 删除从第0个到第1个，包含首尾元素
# listbox.delete(1)   # 删除第1个

# 选中
listbox.select_set(2,5)
# listbox.select_set(4)
# 取消选中
# listbox.selection_clear(2,4) # 包含首尾
# listbox.selection_clear(3)
# 获取元素个数
print(listbox.size())
# 取值
print(listbox.get(2,4))
print(listbox.get(2))

# 获取被选中项的下标，
print(listbox.curselection()) # 也就是索引项，返回结果是一个元组

# 判断一个选项是否被选中
print(listbox.selection_includes(3))




win.mainloop()