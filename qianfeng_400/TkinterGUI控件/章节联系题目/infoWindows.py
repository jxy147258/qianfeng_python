# 在层级目录中点击某个文件，显示它的内容
import  tkinter



class InfoWindows(tkinter.Frame):
    def __init__(self,master):
        frame = tkinter.Frame(master)
        # frame.grid(row=0,column=1) # 目的是原来已经有一个frame，这个新的frame摆在原来的右边
        frame.pack(side=tkinter.RIGHT,fill=tkinter.Y)

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()


        self.text = tkinter.Text(frame)
        self.text.pack()

