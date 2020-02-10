import  tkinter
from tkinter import ttk
import os


def getLastPath(path):
    pathList = os.path.split(path)
    return pathList[-1]


class TreeWindows(tkinter.Frame):
    def __init__(self,master,path,otherwin):
        frame =tkinter.Frame(master)
        frame.pack()
        self.otherwin = otherwin
        self.tree = ttk.Treeview(frame)
        self.tree.pack()

        root = self.tree.insert("", "end", text=getLastPath(path), open=True,values=(path))
        self.loadTree(root,path)
        
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

    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            # 插入树枝
            treey = self.tree.insert(parent,'end', text=getLastPath(absPath),values = (absPath))
            # 判断是否是目录
            if os.path.isdir(absPath):
                self.loadTree(treey,absPath)


