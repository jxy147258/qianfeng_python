import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


# Button-1 单击鼠标左键
# Button-2 单击鼠标滚轮
# Button-3 单击鼠标右键
# Double-Button-1 单击鼠标左键
# Double-Button-3 单击鼠标右键

label1 = tkinter.Label(win,text="鼠标左键") # 换成Button按钮也行，其他的也行
def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print(event.x,event.y)
# bind 给控件绑定事件
# B1-Motion 左键拖动
# B2-Motion 中键拖动
# B3-Motion 右键拖动
label1.bind("<B1-Motion>",func)
label1.bind("<B2-Motion>",func)
label1.bind("<B3-Motion>",func)
label1.pack()

win.mainloop()