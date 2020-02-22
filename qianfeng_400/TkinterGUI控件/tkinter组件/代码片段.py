import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.title("左右排列")
# win.geometry("400x400+200+100")



frame1 = tkinter.Frame(win)
frame2 = tkinter.Frame(win)

text1 = tkinter.Text(frame1)
text2 = tkinter.Text(frame2)
text1.pack()
text2.pack()


frame1.pack(side = tkinter.LEFT,fill = tkinter.Y)
frame2.pack(side = tkinter.RIGHT,fill = tkinter.Y)



win.mainloop()