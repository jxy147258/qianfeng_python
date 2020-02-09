import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


tree = ttk.Treeview(win)
tree.pack()




win.mainloop()