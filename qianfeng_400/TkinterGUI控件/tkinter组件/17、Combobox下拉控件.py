import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


combovariabel = tkinter.StringVar()
combobox = ttk.Combobox(win,textvariable = combovariabel)
combobox.pack()
# 设置下拉数据
combobox["values"] = ["黑龙江","吉林","辽宁"]
# 设置下拉数据的默认值
combobox.current(0)

def func(event):
    print(combovariabel.get())

combobox.bind("<<ComboboxSelected>>",func)



win.mainloop()