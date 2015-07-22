import java.util.Scanner;


/**
 * @author Sahid S Almas
 */
 
public class Converto {
    private static Scanner mScanner;
    private static int SELECTED_ON_ENG_TO_ARA = 1;
    private static int SELECTED_ON_ARA_TO_ENG = 2;
    private static int SELECTED_ON_ABOUT_PI_DEV = 3;
    private static int SELECTED_STATUS = 0;
    private static String TEXT;
    public static void main(String[] args) {
        mScanner = new Scanner(System.in);
        sys("Welcome to Converto by PI-Developers \n");
        sys("Please select any one of this \n");
        sys("1) Would you like to change your mistyped text from english to arabic \n");
        sys("1) Would you like to change your mistyped text from arabic to english \n");
        sys("3) About Pi Developers \n");
        sys("Enter value : ");
        do {
            SELECTED_STATUS = mScanner.nextInt();

            if (SELECTED_STATUS == SELECTED_ON_ENG_TO_ARA ) {
                performENGtoAra();
            } else if (SELECTED_STATUS == SELECTED_ON_ARA_TO_ENG) {
                performAratoEng();
            } else if (SELECTED_STATUS == SELECTED_ON_ABOUT_PI_DEV ) {
                performAboutPi();
            } else if (SELECTED_STATUS != 1 && SELECTED_STATUS != 2 && SELECTED_STATUS != 3) {
                sys("Please Enter Correct Value ");
            }
        }while (mScanner.hasNextInt());
    }

    private static void performAboutPi() {
        sys("Converto 2015 by Pi Developers \n");
        sys("Developers \n");
        sys("Sahid S Almas (in java)");
        sys("Mohammad Rashad (in pyathon)");
        System.exit(0);
    }

    private static void performAratoEng() {
        sys("Please Enter Your Text in lower case:\n");
        do {
            TEXT = mScanner.next();
            if (TEXT == null) {
                sys("Please enter something ");
                System.exit(0);
            } else  {
                String x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,
                        x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35;
                x1 = TEXT.replace("ض" , "q");;
                x2 = x1.replace("ص" , "w");;
                x3 = x2.replace("ث" , "e");;
                x4 = x3.replace("ق" , "r");;
                x5 = x4.replace("ف" , "t");;
                x6 = x5.replace("غ" , "y");;
                x7 = x6.replace("ع" , "u");;
                x8 = x7.replace("ه" , "i");;
                x9 = x8.replace("خ" , "o");;
                x10 = x9.replace("ح" , "p");
                x11 = x10.replace("ج" , "[");;
                x12 = x11.replace("د" , "]");
                x13 = x12.replace("ش" , "a");
                x14 = x13.replace("س" , "s");
                x15 = x14.replace("ي" , "d");
                x16 = x15.replace("ب" , "f");
                x17 = x16.replace("ل" , "g");
                x18 = x17.replace("ا" , "h");
                x19 = x18.replace("أ" , "h");
                x20 = x19.replace("ت" , "j");
                x21 = x20.replace("ن" , "k");
                x22 = x21.replace("م" , "l");
                x23 = x22.replace("ك" , ";");
                x24 = x23.replace("ط" , "'");
                x25 = x24.replace("ئ" , "z");
                x26 = x25.replace("ء" , "x");
                x27 = x26.replace("ؤ" , "c");
                x28 = x27.replace("ر" , "v");
                x29 = x28.replace("ى" , "n");
                x30 = x29.replace("ة" , "m");
                x31 = x30.replace("و" , ",");
                x32 = x31.replace("ز" , ".");
                x33 = x32.replace("ظ" , "/");
                x34 = x33.replace("ذ" , "`");
                x35 = x34.replace("ﻻ" , "b");

                sys("\n Processing ...");
                sys("\n Your text are below :");
                sys(x34);
                System.exit(0);
            }
        } while (mScanner.hasNext());

    }

    private static void performENGtoAra() {
        sys("Please Enter Your Text in lower case:\n");
        do {
            TEXT = mScanner.next();
            if (TEXT == null) {
                sys("Please enter something ");
                System.exit(0);
            } else  {
                String x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,
                        x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34;
                x1 = TEXT.replace("q","ض");
                x2 = x1.replace("w" , "ص");
                x3 = x2.replace("e" , "ث");
                x4 = x3.replace("r", "ق" );
                x5 = x4.replace( "t" , "ف");
                x6 = x5.replace("y" , "غ");
                x7 = x6.replace("u" , "ع");
                x8 = x7.replace( "i" , "ه");
                x9 = x8.replace("o" , "خ");
                x10 = x9.replace("p" , "ح");
                x11 = x10.replace( "[" ,"ج" );
                x12 = x11.replace("]" ,"د"  );
                x13 = x12.replace("a" ,"ش"  );
                x14 = x13.replace( "s" , "س");
                x15 = x14.replace("d" , "ي"  );
                x16 = x15.replace("f" , "ب"  );
                x17 = x16.replace("g" ,"ل");;
                x18 = x17.replace("h" , "ا" );;
                x19 = x18.replace( "h" ,"أ" );
                x20 = x19.replace("j" ,"ت" );
                x21 = x20.replace("k" ,"ن"  );
                x22 = x21.replace("l" ,"م"  );
                x23 = x22.replace(";" ,"ك"  );
                x24 = x23.replace("'" , "ط");
                x25 = x24.replace("z" , "ئ");
                x26 = x25.replace("x" ,"ء"  );
                x27 = x26.replace("c" ,"ؤ");
                x28 = x27.replace("v" , "ر" );
                x29 = x28.replace( "n" ,"ى");
                x30 = x29.replace("m" ,"ة" );
                x31 = x30.replace("m" , "و" );
                x32 = x31.replace("." ,"ز" );
                x33 = x32.replace("/" , "ظ" );
                x34 = x33.replace("`" , "ذ");
                sys("\n Processing ...");
                sys("\n Your text are below :");
                sys(x34);
                System.exit(0);
            }
        } while (mScanner.hasNext());
    }

    private static void sys(Object object) {
        System.out.println(object);
    }

}
