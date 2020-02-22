import  tkinter
from tkinter import ttk
import os


def getLastPath(path):
    pathList = os.path.split(path)
    return pathList[-1]


class TreeWindows():# tkinter.Frame
    def __init__(self,master,path,otherwin):
        frame =tkinter.Frame(master)
        frame.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.otherwin = otherwin
        self.path = path

        self.tree = ttk.Treeview(frame)
        self.tree.pack()

        root = self.tree.insert("", "end", text=getLastPath(self.path), open=True,values=(self.path))
        self.loadTree(root,self.path)
        
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)

        # 给tree绑定点击事件
        self.tree.bind("<<TreeviewSelect>>",self.func)
    def func(self,event):
        # 提取出文件的名称
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)["text"]
            self.otherwin.ev.set(file)
            apath = self.tree.item(sv)["values"][0]
            # 点击鼠标显示文件内容
            if not os.path.isdir(file):
                self.otherwin.text.delete(0.0,tkinter.END)
                self.otherwin.text.insert(tkinter.INSERT,self.readtext())
    # 理想状态是先获取到鼠标点击的文件名是什么，然后再判断是不是file，是就都内容
    def readtext(self):
        return "这里本应该是文本内容"



    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            # 插入树枝
            # treey = self.tree.insert(parent,'end', text=getLastPath(absPath),values = (absPath)) # 老师讲的做法
            treey = self.tree.insert(parent,'end', text=fileName,values = (absPath))  # 自己做法，区别在text怎么得到的

            # 判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey,absPath)


