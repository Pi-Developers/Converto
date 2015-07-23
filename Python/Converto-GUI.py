# -*- coding: utf-8 -*-
#!/usr/bin/python3


#author @mohamed rashad


import sys  
import Tkinter
import subprocess
import tkMessageBox

from Tkinter import *



reload(sys)  
sys.setdefaultencoding('utf8')


#####################

root = Tkinter.Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry('{}x{}'.format(600, 180))
root.wm_title("Converto - The Ultimate Text Fixer (Linux/Unix Edition)")


#####################


about_pi = """- Who are we ?
\nA tech startup.Wwe are Egyptians, a group of teenagers with vision and mind. we want to make computer (PC, mobile..etc) users usage better and easier by offering new solutions.
\n\n
- our goal ?
\nTo reach the greatest potential with your device and make you -the user- satisfied.
\nby using our solutions, your life will be better.
\nUser comes first, all this work is for you, and every person is potentially a user, so you all matter to us.We work for you.
\n\n
- Our philosophy ?
\nWe were born to innovate , not to copy others. We follow this slogan as it is the bible, since our launch we have been creating ideas, or refining others, we will not settle for normal when we can reach for the stars.

\n\nif you like our humble work, just share it, that's better than money :D
\n\n\n_____________________________________
\nVisit us here:
\nhttps://www.facebook.com/PiDevs
\nhttps://twitter.com/pi_developers
\nhttp://www.pi-developers.com
\nhttp://pidevelopers.blogspot.com"""



about_app = """Converto
\nThe app that will make your keyboard experience better, no need to worry about forgetting to switch your keyboard language before typing anymore...
\n\n
Reason to create this?
\nTechnology was made to make you feel comforted, this will help you and save your "Damn ,I forgot to change keyboard language"
Totally worth it!
\n\nThis app is :
\n-Cross Platform : no matter what your PC runs, you can use Converto
\n-Multi Lingual : coded in python, java and vb.net to provide many solutions for users with one of them not installed
\n-Easy to use : no installation or anything, use out-of-box
\n-Open source : everyone can contribute to development
\n\nHave fun using our app, Feedback is welcomed..""" 



#####################


def show1():
    
        tkMessageBox.showinfo( "About Pi Developers" , about_pi )

#####################

def show2():

        tkMessageBox.showinfo( "About Converto", about_app)

#####################

b0 = Button(root, text="About Converto", command=show2)
b0.pack(side=BOTTOM,fill=X ,expand="yes",padx=5,pady=0)
b00 = Button(root, text="About Pi Developers", command=show1)
b00.pack(side=BOTTOM,fill=X ,expand="yes",padx=5,pady=3)

#####################

labelframe = LabelFrame(root, text="English to Arabic")
labelframe.pack(fill="both", expand="yes",side=LEFT ,padx=10 ,pady=3)
labelframe1 = LabelFrame(root, text="Arabic to English")
labelframe1.pack(fill="both", expand="yes",side=LEFT ,padx=10 ,pady=3)

#####################

right = Label(labelframe, text="Write/Paste English text here :")
right.pack(padx=4 ,pady=4)
left = Label(labelframe1, text="Write/Paste Arabic text here :")
left.pack(padx=4 ,pady=4)
 
#####################

e = Entry(labelframe1 ,textvariable="hey")
e.pack(padx=3 ,pady =1,fill=X)

f = Entry(labelframe ,text="fbfb",textvariable="you")
f.pack(padx=3,pady =1,fill=X)

#####################


def pastea():

        f.insert(0, root.clipboard_get())


#####################
def pastee():

        e.insert(0, root.clipboard_get())


#####################

def cone():

        x0 = e.get()

        x1 = x0.replace("ض" , "q")
        x2 = x1.replace("ص" , "w")
        x3 = x2.replace("ث" , "e")
        x4 = x3.replace("ق" , "r")
        x5 = x4.replace("ف" , "t")
        x6 = x5.replace("غ" , "y")
        x7 = x6.replace("ع" , "u")
        x8 = x7.replace("ه" , "i")
        x9 = x8.replace("خ" , "o")
        x10 = x9.replace("ح" , "p")
        x11 = x10.replace("ج" , "[")
        x12 = x11.replace("د" , "]")
        x13 = x12.replace("ش" , "a")
        x14 = x13.replace("س" , "s")
        x15 = x14.replace("ي" , "d")
        x16 = x15.replace("ب" , "f")
        x17 = x16.replace("ل" , "g")
        x18 = x17.replace("ا" , "h")
        x19 = x18.replace("أ" , "h")
        x20 = x19.replace("ت" , "j")
        x21 = x20.replace("ن" , "k")
        x22 = x21.replace("م" , "l")
        x23 = x22.replace("ك" , ";")
        x24 = x23.replace("ط" , "'")
        x25 = x24.replace("ئ" , "z")
        x26 = x25.replace("ء" , "x")
        x27 = x26.replace("ؤ" , "c")
        x28 = x27.replace("ر" , "v")
        x29 = x28.replace("ى" , "n")
        x30 = x29.replace("ة" , "m")
        x31 = x30.replace("و" , ",")
        x32 = x31.replace("ز" , ".")
        x33 = x32.replace("ظ" , "/")
        x34 = x33.replace("ذ" , "`")
        global x35
        x35 = x34.replace("ﻻ" , "b")

        e.delete(0 , 'end')
        e.insert(0 , x35)


#####################

def copy():

        root.clipboard_clear()
        root.clipboard_append(x35)

####################
def cona():

        x0 = f.get()

        x1 = x0.replace("q","ض")
        x2 = x1.replace("w" , "ص")
        x3 = x2.replace("e" , "ث")
        x4 = x3.replace("r", "ق" )
        x5 = x4.replace( "t" , "ف")
        x6 = x5.replace("y" , "غ")
        x7 = x6.replace("u" , "ع")
        x8 = x7.replace( "i" , "ه")
        x9 = x8.replace("o" , "خ")
        x10 = x9.replace("p" , "ح")
        x11 = x10.replace( "[" ,"ج" )
        x12 = x11.replace("]" ,"د"  )
        x13 = x12.replace("a" ,"ش"  )
        x14 = x13.replace( "s" , "س")
        x15 = x14.replace("d" , "ي"  )
        x16 = x15.replace("f" , "ب"  )
        x17 = x16.replace("g" ,"ل")
        x18 = x17.replace("h" , "ا" )
        x19 = x18.replace( "h" ,"أ" )
        x20 = x19.replace("j" ,"ت" )
        x21 = x20.replace("k" ,"ن"  )
        x22 = x21.replace("l" ,"م"  )
        x23 = x22.replace(";" ,"ك"  )
        x24 = x23.replace("'" , "ط")
        x25 = x24.replace("z" , "ئ")
        x26 = x25.replace("x" ,"ء")
        x27 = x26.replace("c" ,"ؤ")
        x28 = x27.replace("v" , "ر")
        x29 = x28.replace( "n" ,"ى")
        x30 = x29.replace("m" ,"ة" )
        x31 = x30.replace("m" , "و" )
        x32 = x31.replace("." ,"ز" )
        x33 = x32.replace("/" , "ظ" )
        global x34
        x34 = x33.replace("`" , "ذ")

        f.delete(0 , 'end')
        f.insert(0 , x34)
     
#####################

def copy1():

        root.clipboard_clear()
        root.clipboard_append(x34)

#####################

b1 = Button(labelframe1, text="Convert",command=cone)
b2 = Button(labelframe, text="Convert",command=cona)
b1.pack(side=LEFT,fill=X ,expand="yes",padx=3 , pady=3)
b2.pack(side=LEFT,fill=X, expand="yes",padx=3, pady=3)

#####################

b3 = Button(labelframe1, text="Copy",command=copy)
b4 = Button(labelframe, text="Copy",command=copy1)
b3.pack(side=LEFT,fill=X ,expand="yes",padx=3, pady=3)
b4.pack(side=LEFT,fill=X, expand="yes",padx=3, pady=3)

#####################

b5 = Button(labelframe1, text="Paste", command=pastee)
b6 = Button(labelframe, text="Paste", command=pastea)
b5.pack(side=LEFT,fill=X ,expand="yes",padx=3, pady=3)
b6.pack(side=LEFT,fill=X, expand="yes",padx=3, pady=3)

#####################

root.mainloop()
