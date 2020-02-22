import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# 通过拖拽指示器改变变量的值，例如音量
scale = tkinter.Scale(win,
                      from_ = 0,
                      to = 100,
                      orient = tkinter.HORIZONTAL, # 默认是竖直方向VERTICAL
                      tickinterval = 10, # 显示刻度，以此值为倍数
                      length = 300


                      )
scale.pack()
# 获取当前值
print(scale.get())
# 另一种获取方式，先定义一个按钮，按下按钮再显示
def shownum():
    print(scale.get())
button = tkinter.Button(win,text = "显示当前值",command = shownum)
button.pack()
# 设置默认值
scale.set(20)
print(scale.get())


win.mainloop()