import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")




label1 = tkinter.Label(win,text="鼠标左键",bg="purple") # 换成Button按钮也行，其他的也行
label1.focus_set()
def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print("event.char:",event.char,"event.keycode:",event.keycode)
    # 当传入按键事件时，可以获取到的变量，event.char是当前按键，code是键上字母对应的ASCII码
# bind 给控件绑定事件
# Key 响应键盘所有按键按下时的事件
label1.bind("<Key>",func)
# 也可以给win主窗体聚焦
#win.bind("<Key>",func)
label1.pack()

win.mainloop()