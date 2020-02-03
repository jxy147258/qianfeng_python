import tkinter as tk

root = tk.Tk()


# v = tk.IntVar()
# c = tk.Checkbutton(root,text="hello",variable=v)
# c.pack()

# l = tk.Label(root,textvariable=v)
# l.pack()



# GIRLS = ["张三","李四","马s武","猴ss六"]
# v = []


# for girl in GIRLS:
#     v.append(tk.IntVar())
#     b = tk.Checkbutton(root,text=girl,variable=v[-1])
#     b.pack(anchor="w")
    


b1 = tk.Checkbutton(root,text="girl1")
b2 = tk.Checkbutton(root,text="girl2")
b3 = tk.Checkbutton(root,text="girl3")
b4 = tk.Checkbutton(root,text="girl4")
b1.pack(anchor="nw")
b2.pack(anchor="ne")
b3.pack(anchor="se")
b4.pack(anchor="sw")    

tk.mainloop()