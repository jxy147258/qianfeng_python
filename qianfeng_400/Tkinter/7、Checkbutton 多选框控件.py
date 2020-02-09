import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")



# Checkbutton 多选框控件


def update():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    # 显示新内容前清除旧内容
    # 从第0行删除到最后一行，写1 就是从0到1行
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.END, message)

hobby1 = tkinter.BooleanVar()
hobby2 = tkinter.BooleanVar()
hobby3 = tkinter.BooleanVar()
checkbutton1 = tkinter.Checkbutton(win,text = "money",variable =hobby1,command = update).pack()
checkbutton2 = tkinter.Checkbutton(win,text = "power",variable =hobby2,command = update).pack()
checkbutton3 = tkinter.Checkbutton(win,text = "people",variable =hobby3,command = update).pack()

text = tkinter.Text(win,width = 50,height = 5)
text.pack()




win.mainloop()