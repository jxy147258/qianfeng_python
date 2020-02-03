# -*- coding: utf-8 -*-

import tkinter as tk


root = tk.Tk()

v = tk.IntVar()

LANGS = [
        ("python",1),
        ("c",2),
        ("C++",3)]
for lang,num in LANGS:
    tk.Radiobutton(root,variable=lang,value= num).pack(anchor="w")

tk.mainloop()