import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

listvariable = tkinter.StringVar()
listbox = tkinter.Listbox(win,
                          width = 100 ,
                          height = 10,
                          selectmode  = tkinter.SINGLE,# 区别于BROWSR的是按下鼠标后
                                                       # 不能移动鼠标来选中
                          listvariable = listvariable

                          )

listbox.pack()
for item in ["good","cool","nice","handsome"]:
    # tkinter.END是从前往后
    listbox.insert(tkinter.END,item)
# 获取所有选项
print(listvariable.get())
# 设置所有选项
listvariable.set(("1", "2", "3"))
print(listvariable.get())
# 绑定事件
def myfunc(event):
    print(listbox.get(listbox.curselection()))
listbox.bind('<Double-Button-1>',myfunc)




win.mainloop()