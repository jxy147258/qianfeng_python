import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

label4 = tkinter.Label(win,text="中国",bg="red").grid(row=0,column=0)
label5 = tkinter.Label(win,text="北京",bg="yellow").grid(row=0,column=1)
label6 = tkinter.Label(win,text="海淀区",bg="yellow").grid(row=1,column=0)
label7 = tkinter.Label(win,text="朝阳区",bg="purple").grid(row=1,column=1)



win.mainloop()