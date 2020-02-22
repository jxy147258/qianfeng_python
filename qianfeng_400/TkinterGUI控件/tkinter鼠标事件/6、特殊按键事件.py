import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")




label1 = tkinter.Label(win,text="鼠标左键",bg="purple") # 换成Button按钮也行，其他的也行
label1.focus_set()
#win.focus_set() # 也可以
def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print("event.char:",event.char,"event.keycode:",event.keycode)
    # 当传入按键事件时，可以获取到的变量，event.char是当前按键，code是键上字母对应的ASCII码
# bind 给控件绑定事件
# 左shift，和右shift
label1.bind("<Shift_L>",func)
label1.bind("<Shift_R>",func)
label1.bind("<Control_R>",func)
# label1.bind("<Caps_Lock>",func) # 不报错，也没有响应
label1.bind("<Tab>",func)
label1.bind("<F5>",func)
label1.bind("<Return>",func)
label1.bind("<BackSpace>",func)
label1.pack()

win.mainloop()