import  tkinter

win = tkinter.Tk()
win.title("sunck")
win.geometry("400x400+100+100")


e = tkinter.Variable()
entry = tkinter.Entry(win,textvariable = e)
entry.pack()

def foo():
    print(e.get())
    
button = tkinter.Button(win,text = "按钮",command = foo)
button.pack()



win.mainloop()