import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


menubar = tkinter.Menu(win)
menubar.config()


win.mainloop()