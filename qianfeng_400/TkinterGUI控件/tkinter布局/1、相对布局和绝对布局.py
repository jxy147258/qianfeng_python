import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# 绝对布局，用label做示例
label1 = tkinter.Label(win,text="中国",bg="red").place(x=10,y=10)
label2 = tkinter.Label(win,text="北京",bg="yellow").place(x=50,y=50)
label3 = tkinter.Label(win,text="朝阳区",bg="purple").place(x=100,y=100)
# 相对布局，用label做示例
# label4 = tkinter.Label(win,text="中国",bg="red").pack(fill = tkinter.X,side=tkinter.TOP)
# label5 = tkinter.Label(win,text="北京",bg="yellow").pack(fill = tkinter.Y,side=tkinter.LEFT)
# label6 = tkinter.Label(win,text="海淀区",bg="yellow").pack(fill = tkinter.Y,side=tkinter.RIGHT)
# label7 = tkinter.Label(win,text="朝阳区",bg="purple").pack(fill = tkinter.X,side=tkinter.BOTTOM)
label8 = tkinter.Label(win,text="朝阳区",bg="purple").pack(fill = tkinter.BOTH,side=tkinter.TOP)


win.mainloop()