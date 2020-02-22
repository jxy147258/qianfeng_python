import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")



# radiobutton 控件
def update():
    print(r.get())
# 一组单选框要绑定同一个变量
r = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(win,text = "one",variable = r,value = 1,command = update).pack()
radiobutton2 = tkinter.Radiobutton(win,text = "two",variable = r,value = 2,command = update).pack()
radiobutton3 = tkinter.Radiobutton(win,text = "three",variable = r,value = 3,command = update).pack()
radiobutton4 = tkinter.Radiobutton(win,text = "four",variable = r,value = 4,command = update).pack()




win.mainloop()