# 用树状布局，显示层级目录
import tkinter
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("层级显示目录")
# win.geometry("400x400+200+100")

path = r"F:\python_G\python_shell"

infowin = InfoWindows(win)
treeWin = TreeWindows(win,path,infowin)



win.mainloop()
