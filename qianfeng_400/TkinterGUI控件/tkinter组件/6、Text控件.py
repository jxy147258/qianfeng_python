import tkinter

win = tkinter.Tk()
win.title("窗口名称")
win.geometry("400x400+200+100")


# Text控件，不带滚动条
# 用于显示多行文本
text1 = tkinter.Text(win,
                    width = 10,  # 字节数
                    height = 10, # 行数

                    )
str1 = '''baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
'''
text1.insert(tkinter.INSERT,str1)
text1.pack()

# 带滚动条的Text
str1 = '''baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
baiyh2baiyh2baiyh2baiyh2baiyh
'''
scrollbar = tkinter.Scrollbar()
text2 = tkinter.Text(win,width= 30,height= 4)
text2.insert(tkinter.INSERT,str1)
scrollbar.pack(side=tkinter.RIGHT,fill = tkinter.Y) # 位置在右侧，Y轴上填充
text2.pack(side=tkinter.LEFT,fill=tkinter.Y) # 位置在左侧，Y轴上填充
# 关联两者
scrollbar.config(command=text2.yview) # 控制滚动条动的时候，文本动
text2.config(yscrollcommand = scrollbar.set)  # 同时文本滚动的同时，滚动条也在动





win.mainloop()