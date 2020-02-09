import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


# Button控件
# def func1():
#     print("sunck is a good man")
# button1 = tkinter.Button(win,
#                         text = "打印1",
#                         command = func1,# 直接写函数名，没有括号（）
#                         width = 10,
#                         height = 10,
#                         )
# button1.pack()
# button2 = tkinter.Button(win,
#                         text = "打印2",
#                         command = lambda:print("sunck is a good man"),
#                         width = 5,
#                         height = 1,
#                         )
# button2.pack()
#
# button3 = tkinter.Button(win,
#                         text = "退出",
#                         command = win.quit,
#                         width = 5,
#                         height = 2,
#                         )
# button3.pack()




win.mainloop()