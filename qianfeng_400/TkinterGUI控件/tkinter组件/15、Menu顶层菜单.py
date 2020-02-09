import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# 创建菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

# 创建一个菜单选项
menu1 = tkinter.Menu(menubar,
                     tearoff = False
                     )
# 给创建好的菜单选项加内容，就是下拉内容
for item in ["c","c++","java",".net","asp.net","html","CSS","javascript"]:
    if item == "退出":
        menu1.add_command(label=item)
    else:
        menu1.add_command(label=item)

# 把菜单选项添加到菜单选项
menubar.add_cascade(label="语言",menu=menu1)


win.mainloop()