import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")



def func(event): # 用bind（）函数一定加这个event参数，用command就不用
    print("event.char:",event.char,"event.keycode:",event.keycode)
    # 当传入按键事件时，可以获取到的变量，event.char是当前按键，code是键上字母对应的ASCII码
# bind 给控件绑定事件
# 自己组合任意按键
win.bind("<Control-Alt-Up>",func) # 不用控件，直接给窗体绑定事件
win.bind("<Shift-Alt-Down>",func) # 不用控件，直接给窗体绑定事件

win.mainloop()