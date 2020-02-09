import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")

# Label 标签
# 属性，win主窗体，text文本，bg背景色，fg字体色
# label1 = tkinter.Label(win,
#                        text="这是label的文本",
#                        bg = "blue",
#                        fg = "red",
#                        #image =r"E:\download_c\eyes.jpg",
#                        font =("微软雅黑 ",20),
#                        width = 10,
#                        height = 1,
#                        wraplength = 50,# 多宽换行
#                        justify = "left",
#                        anchor = "w",#文本东西南北哪个方位，n，s，e，w，以及两者结合，center
#                         )
# label1.pack()



win.mainloop()