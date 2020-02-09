import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

listvariable = tkinter.StringVar()
listbox = tkinter.Listbox(win,
                          width = 100 ,
                          height = 10,
                          selectmode  = tkinter.MULTIPLE,# 已经学了SINGLE，BROWSE，EXTENDED，MULTIPLE
                                                       # MULTIPLE
                          listvariable = listvariable

                          )

for item in ["good","cool","nice","handsome","good","cool","nice","handsome","good","cool","nice","handsome","good","cool","nice","handsome"]:
    # tkinter.END是从前往后
    listbox.insert(tkinter.END,item)

listbox.pack()

win.mainloop()