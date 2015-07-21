# -*- coding: utf-8 -*-
#!/usr/bin/python

while True:

    print "\n\n   ~~~~~~~~~~~~~~~~~~Welcome to Converto Script~~~~~~~~~~~~~~~~~~~"

    print "\n Would you like to fix..?\n\t1-Arabic to English\n\t2-English to Arabic"

    print "\n Choose your Option:"

    Input = raw_input(">")

    if Input == "1":
    
        print "\n Enter your arabic mistyped text:"
        input2 = raw_input("> ")

        print "\n\n Proccessing.."
        x1 = input2.replace("ض" , "q")
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
        x35 = x34.replace("ﻻ" , "b")

        print "\n\n Your Text : " ,
        print x35


    
    elif Input == "2":    

        print "Enter your english mistyped text:"
        input2 = raw_input(">")

        print "\n\n Proccessing.."
        x1 = input2.replace("q","ض")
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
        x26 = x25.replace("x" ,"ء"  )
        x27 = x26.replace("c" ,"ؤ")
        x28 = x27.replace("v" , "ر"  )
        x29 = x28.replace( "n" ,"ى")
        x30 = x29.replace("m" ,"ة" )
        x31 = x30.replace("m" , "و" )
        x32 = x31.replace("." ,"ز" )
        x33 = x32.replace("/" , "ظ" )
        x34 = x33.replace("`" , "ذ")

        print "\n\n Your Text : " ,
        print x34





