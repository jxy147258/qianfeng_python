import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

listvariable = tkinter.StringVar()
listbox = tkinter.Listbox(win,
                          width = 100 ,
                          height = 10,
                          selectmode  = tkinter.EXTENDED,# 已经学了SINGLE，BROWSE，EXTENDED，
                                                       # EXTENDED用来支持shift和control
                          listvariable = listvariable

                          )

for item in ["good","cool","nice","handsome","good","cool","nice","handsome","good","cool","nice","handsome","good","cool","nice","handsome"]:
    # tkinter.END是从前往后
    listbox.insert(tkinter.END,item)

# 安住shift，实现连选，按住control，实现多选
# 测试shift和control

# 滚动条
sc = tkinter.Scrollbar()
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
sc["command"] = listbox.yview
listbox.configure(yscrollcommand=sc.set)
listbox.pack(side=tkinter.LEFT,fill=tkinter.BOTH)




win.mainloop()