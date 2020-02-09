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
def printmyteacher():
    print(" sunck is a good man")
for item in ["c","c++","java",".net","asp.net","html","CSS","javascript","退出"]:
    if item == "退出":
        # 增加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command = win.quit)
    else:
        menu1.add_separator()
        menu1.add_command(label=item,command = printmyteacher)

# 把菜单选项添加到菜单选项
menubar.add_cascade(label="语言",menu=menu1)
menubar.add_cascade(label="语言",menu=menu1)

# 再多加一个菜单
menu2 = tkinter.Menu(menubar,tearoff = False)
menu2.add_command(label="red")
menu2.add_command(label="orange")
menu2.add_command(label="yellow")
menu2.add_command(label="green")
menubar.add_cascade(label="颜色",menu=menu2)
menubar.add_cascade(label="颜色",menu=menu2)


win.mainloop()