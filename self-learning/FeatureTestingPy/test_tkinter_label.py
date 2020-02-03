
"""
1，同一个root框上，左边显示文字，右边显示图片
2，点击button，显示的文本发生变化
"""
from tkinter import *

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

def callback():
    var.set("不信")
photo= PhotoImage(file="18.png")
var = StringVar()
var.set("未满18，禁止")
label = Label(frame1,textvariable=var,justify=LEFT)
label.pack(side = LEFT)
imagelable = Label(frame1,image=photo)
imagelable.pack()

    
button = Button(frame2,text="已经满18",command=callback)
button.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

if __name__ == "__main__":
    root.mainloop()