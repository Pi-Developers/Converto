#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter
from Tkinter import *

root = Tkinter.Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(600, 170))
root.wm_title("Converto - The Ultimate Text Fixer (Linux Edition)")


b0 = Button(root, text="About Converto")
b0.pack(side=BOTTOM,fill=X ,expand="yes",padx=5,pady=5)
b0 = Button(root, text="About Pi Developers")
b0.pack(side=BOTTOM,fill=X ,expand="yes",padx=5,pady=3)


labelframe = LabelFrame(root, text="English to Arabic")
labelframe.pack(fill="both", expand="yes",side=LEFT ,padx=10 ,pady=0)
labelframe1 = LabelFrame(root, text="Arabic to English")
labelframe1.pack(fill="both", expand="yes",side=LEFT ,padx=10 ,pady=0)


right = Label(labelframe, text="Write/Paste English text here :")
right.pack(padx=4 ,pady=4)
left = Label(labelframe1, text="Write/Paste Arabic text here :")
left.pack(padx=4 ,pady=4)
 


e = Entry(labelframe1 ,textvariable="hey")
e.pack(padx=2 ,pady =1,fill=X)
f = Entry(labelframe ,text="fbfb",textvariable="you")
f.pack(padx=2,pady =1,fill=X)


b1 = Button(labelframe1, text="Convert")
b2 = Button(labelframe, text="Convert")
b3 = Button(labelframe1, text="Copy")
b4 = Button(labelframe, text="Copy")


b1.pack(side=LEFT,fill=X ,expand="yes",padx=3)
b2.pack(side=LEFT,fill=X, expand="yes",padx=3)
b3.pack(side=LEFT,fill=X ,expand="yes",padx=3)
b4.pack(side=LEFT,fill=X, expand="yes",padx=3)






root.mainloop()
