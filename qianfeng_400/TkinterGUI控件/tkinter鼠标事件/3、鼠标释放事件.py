import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")




label1 = tkinter.Label(win,text="鼠标左键",bg="purple") # 换成Button按钮也行，其他的也行
def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print(event.x,event.y)
# bind 给控件绑定事件
# ButtonRelease-1 单击鼠标左键
# ButtonRelease-2 单击鼠标中键
# ButtonRelease-3 单击鼠标右键
label1.bind("<Button-1>",func)
label1.bind("<ButtonRelease-1>",func)
label1.bind("<ButtonRelease-2>",func)
label1.bind("<ButtonRelease-3>",func)

label1.pack()

win.mainloop()