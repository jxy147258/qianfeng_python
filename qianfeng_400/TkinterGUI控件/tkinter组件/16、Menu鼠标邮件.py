import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


menubar = tkinter.Menu(win)
# menubar.config()

menu1 = tkinter.Menu(menubar,
                     tearoff = False
                     )

# 给创建好的菜单选项加内容，就是下拉内容
def printmyteacher():
    print(" sunck is a good man")
for item in ["c","c++","java",".net","asp.net","html","CSS","javascript","退出"]:
    menu1.add_command(label=item)

win.mainloop()