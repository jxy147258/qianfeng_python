import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

def update():
    print(spinvariable.get())
spinvariable = tkinter.StringVar()
spinbox = tkinter.Spinbox(win,
                          from_=0,
                          to = 100,
                          increment = 2, # 步长
                          # values = (0,2,4,5,6,8) # 此值不与上述三件套同时使用
                          textvariable = spinvariable,
                          command = update # 值改变就自动触发command
                          ).pack()
# spinvariable.set(20) # 设置默认值，也可以设置成字符串


win.mainloop()