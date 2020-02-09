import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


'''
+----------------------+
+  +-----+   +-----+   +
+  +     +   +     +   +
+  +-----+   +-----+   +
+  +-----+   +-----+   +
+  +     +   +     +   +
+  +-----+   +-----+   +
+----------------------+
先创建一个fram，再创建2个小fram，

'''

fram = tkinter.Frame(win)


fram1 = tkinter.Frame(fram)
fram2 = tkinter.Frame(fram)

label1 = tkinter.Label(fram1,text="左上",bg="pink").pack(side=tkinter.TOP)
label2 = tkinter.Label(fram1,text="左下",bg="orange").pack(side=tkinter.TOP)
fram1.pack(side=tkinter.LEFT)
label3 = tkinter.Label(fram2,text="右上",bg="yellow").pack(side=tkinter.TOP)
label4 = tkinter.Label(fram2,text="右下",bg="purple").pack(side=tkinter.TOP)
fram2.pack(side=tkinter.RIGHT)

fram.pack()

win.mainloop()