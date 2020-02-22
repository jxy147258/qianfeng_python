import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")




label1 = tkinter.Label(win,text="鼠标左键",bg="purple") # 换成Button按钮也行，其他的也行

def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print(event.x,event.y)
# bind 给控件绑定事件
# Enter 光标进入控件
label1.bind("<Enter>",func)
# Leave 光标离开事件
label1.bind("<Leave>",func)
label1.pack()

win.mainloop()