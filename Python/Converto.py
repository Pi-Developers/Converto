# -*- coding: utf-8 -*-
#!/usr/bin/python
#
#author @mohamed rashad
#
import readline 

EnglishPattle = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ[]'/;.,"
ArabicPattle = "شﻻؤيثبلاهتنمةىخحضقسفعرضءغئ"

class Converto:

    def showIntro(self):

        print "\n\n   ~~~~~~~~~~~~~~~~~~Welcome to Converto Script~~~~~~~~~~~~~~~~~~~\nExit code: ^D\n"

    def convert(self,phrase):
        try:
            phrase[0]
        except IndexError:
            return ""
      
        if phrase[0] in EnglishPattle:

            phrase=phrase.replace("q","ض")
            phrase=phrase.replace("w" , "ص")
            phrase=phrase.replace("e" , "ث")
            phrase=phrase.replace("r", "ق" )
            phrase=phrase.replace( "t" , "ف")
            phrase=phrase.replace("y" , "غ")
            phrase=phrase.replace("u" , "ع")
            phrase=phrase.replace( "i" , "ه")
            phrase=phrase.replace("o" , "خ")
            phrase=phrase.replace("p" , "ح")
            phrase=phrase.replace( "[" ,"ج" )
            phrase=phrase.replace("]" ,"د"  )
            phrase=phrase.replace("a" ,"ش"  )
            phrase=phrase.replace( "s" , "س")
            phrase=phrase.replace("d" , "ي"  )
            phrase=phrase.replace("f" , "ب"  )
            phrase=phrase.replace("g" ,"ل")
            phrase=phrase.replace("h" , "ا" )
            phrase=phrase.replace( "h" ,"أ" )
            phrase=phrase.replace("j" ,"ت" )
            phrase=phrase.replace("k" ,"ن"  )
            phrase=phrase.replace("l" ,"م"  )
            phrase=phrase.replace(";" ,"ك"  )
            phrase=phrase.replace("'" , "ط")
            phrase=phrase.replace("z" , "ئ")
            phrase=phrase.replace("x" ,"ء"  )
            phrase=phrase.replace("c" ,"ؤ")
            phrase=phrase.replace("v" , "ر"  )
            phrase=phrase.replace( "n" ,"ى")
            phrase=phrase.replace("m" ,"ة" )
            phrase=phrase.replace("m" , "و" )
            phrase=phrase.replace("." ,"ز" )
            phrase=phrase.replace("/" , "ظ" )
            phrase=phrase.replace("`" , "ذ")
            return phrase


        if phrase[0] in ArabicPattle:

            phrase=phrase.replace("ض" , "q")
            phrase=phrase.replace("ص" , "w")
            phrase=phrase.replace("ث" , "e")
            phrase=phrase.replace("ق" , "r")
            phrase=phrase.replace("ف" , "t")
            phrase=phrase.replace("غ" , "y")
            phrase=phrase.replace("ع" , "u")
            phrase=phrase.replace("ه" , "i")
            phrase=phrase.replace("خ" , "o")
            phrase=phrase.replace("ح" , "p")
            phrase=phrase.replace("ج" , "[")
            phrase=phrase.replace("د" , "]")
            phrase=phrase.replace("ش" , "a")
            phrase=phrase.replace("س" , "s")
            phrase=phrase.replace("ي" , "d")
            phrase=phrase.replace("ب" , "f")
            phrase=phrase.replace("ل" , "g")
            phrase=phrase.replace("ا" , "h")
            phrase=phrase.replace("أ" , "h")
            phrase=phrase.replace("ت" , "j")
            phrase=phrase.replace("ن" , "k")
            phrase=phrase.replace("م" , "l")
            phrase=phrase.replace("ك" , ";")
            phrase=phrase.replace("ط" , "'")
            phrase=phrase.replace("ئ" , "z")
            phrase=phrase.replace("ء" , "x")
            phrase=phrase.replace("ؤ" , "c")
            phrase=phrase.replace("ر" , "v")
            phrase=phrase.replace("ى" , "n")
            phrase=phrase.replace("ة" , "m")
            phrase=phrase.replace("و" , ",")
            phrase=phrase.replace("ز" , ".")
            phrase=phrase.replace("ظ" , "/")
            phrase=phrase.replace("ذ" , "`")
            phrase=phrase.replace("ﻻ" , "b")

            return phrase;

        else: return "please input Arabic or English keyboard letters"

    def getString(self):

        try:
            shit = raw_input("> ")
            return shit;
        except EOFError:
            print "\n"
            exit()

    def mainLoop(self):
        
        while True:
            print self.convert(self.getString());


if __name__ == '__main__':
        Converto().showIntro();
        Converto().mainLoop();
