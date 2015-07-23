import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * @author Sahid S Almas
 */
public class ConvertoGUI {
    public static  String INPUT = null;
    public static void main(String[] args) {
        final JFrame frame = new JFrame("Converto");
        MenuBar jMenuBar = new MenuBar();
        Menu con = new Menu("Converto");
        con.getAccessibleContext().setAccessibleDescription(
                "The only menu in this program that has menu items");
        jMenuBar.add(con);
        MenuItem about = new MenuItem("About");
        about.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                JOptionPane.showMessageDialog(frame,"Who are we ? \n" +
                        "A tech startup.we are Egyptians and Indian, a group of teenagers \n" +
                        " with vision and mind. we want to make computer (PC, mobile..etc) \n" +
                        "users usage better and easier by offering new solutions" +
                        "\n \n"+
                " What is our goal ?"+
                "\n To reach the greatest potential with your device and make you -the user- \n satisfied.\n" +
                        "by using our solutions, your life will be better." +
                        "\n User comes first, all this work is for you, and every person is \n" +
                        " potentially a user, so you all matter to us.We work for you." +
                        "\n \n"+
                        "Our philosophy ?"+
                "We were born to innovate , not to copy others. \n We follow this slogan as it is \n " +
                        "the bible, since our launch we have been creating ideas, or refining \n " +
                        "others, we will not settle for normal when we can reach for the stars"+
                "\n\\nif you like our humble work, just share it, that's better than money :D\n" +
                        "\n\n\n_____________________________________\n" +
                        "\nVisit us here:\n" +
                        "\nhttps://www.facebook.com/PiDevs\n" +
                        "\nhttps://twitter.com/pi_developers\n" +
                        "\nhttp://www.pi-developers.com\n" +
                        "\nhttp://pidevelopers.blogspot.com\"");
            }
        });
        con.add(about);
        frame.setMenuBar(jMenuBar);

        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        final JEditorPane helpPane=new JEditorPane("text",null);
        helpPane.setEditable(true);
        helpPane.setPreferredSize(new Dimension(400, 100));
        helpPane.setText("Please Enter Your text here to fix your mistyped text");

        final JScrollPane helpPanelScrollPane = new JScrollPane(helpPane);

        panel.add(helpPanelScrollPane);


        final JRadioButton option1 = new JRadioButton("English to Arabic",true);
        final JRadioButton option2 = new JRadioButton("Arabic to English");
        ButtonGroup group = new ButtonGroup();
        group.add(option1);
        group.add(option2);
        panel.add(option1);
        panel.add(option2);
        JButton tra = new JButton("Change It");
        helpPane.getText().toLowerCase();
        JButton copy = new JButton("Copy");
        copy.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                helpPane.copy();
            }
        });
        panel.add(copy);

        JButton paste = new JButton("Paste");
        paste.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                helpPane.paste();
            }
        });
        panel.add(paste);
        panel.add(tra);
        tra.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent actionEvent) {
                INPUT = helpPane.getText();
                String a = INPUT.toLowerCase();
                if (option1.isSelected()) {
                    String x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
                            x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34;
                    x1 = a.replace("q", "ض");
                    x2 = x1.replace("w", "ص");
                    x3 = x2.replace("e", "ث");
                    x4 = x3.replace("r", "ق");
                    x5 = x4.replace("t", "ف");
                    x6 = x5.replace("y", "غ");
                    x7 = x6.replace("u", "ع");
                    x8 = x7.replace("i", "ه");
                    x9 = x8.replace("o", "خ");
                    x10 = x9.replace("p", "ح");
                    x11 = x10.replace("[", "ج");
                    x12 = x11.replace("]", "د");
                    x13 = x12.replace("a", "ش");
                    x14 = x13.replace("s", "س");
                    x15 = x14.replace("d", "ي");
                    x16 = x15.replace("f", "ب");
                    x17 = x16.replace("g", "ل");

                    x18 = x17.replace("h", "ا");

                    x19 = x18.replace("h", "أ");
                    x20 = x19.replace("j", "ت");
                    x21 = x20.replace("k", "ن");
                    x22 = x21.replace("l", "م");
                    x23 = x22.replace(";", "ك");
                    x24 = x23.replace("'", "ط");
                    x25 = x24.replace("z", "ئ");
                    x26 = x25.replace("x", "ء");
                    x27 = x26.replace("c", "ؤ");
                    x28 = x27.replace("v", "ر");
                    x29 = x28.replace("n", "ى");
                    x30 = x29.replace("m", "ة");
                    x31 = x30.replace("m", "و");
                    x32 = x31.replace(".", "ز");
                    x33 = x32.replace("/", "ظ");
                    x34 = x33.replace("`", "ذ");
                    helpPane.setText(x34);
                } else if (option2.isSelected()) {
                    String aa = INPUT.toLowerCase();
                    String x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20,
                            x21, x22, x23, x24, x25, x26, x27, x28, x29, x30, x31, x32, x33, x34, x35;
                    x1 = aa.replace("ض", "q");
                    x2 = x1.replace("ص", "w");
                    x3 = x2.replace("ث", "e");
                    x4 = x3.replace("ق", "r");
                    x5 = x4.replace("ف", "t");
                    x6 = x5.replace("غ", "y");
                    x7 = x6.replace("ع", "u");

                    x8 = x7.replace("ه", "i");

                    x9 = x8.replace("خ", "o");

                    x10 = x9.replace("ح", "p");
                    x11 = x10.replace("ج", "[");

                    x12 = x11.replace("د", "]");
                    x13 = x12.replace("ش", "a");
                    x14 = x13.replace("س", "s");
                    x15 = x14.replace("ي", "d");
                    x16 = x15.replace("ب", "f");
                    x17 = x16.replace("ل", "g");
                    x18 = x17.replace("ا", "h");
                    x19 = x18.replace("أ", "h");
                    x20 = x19.replace("ت", "j");
                    x21 = x20.replace("ن", "k");
                    x22 = x21.replace("م", "l");
                    x23 = x22.replace("ك", ";");
                    x24 = x23.replace("ط", "'");
                    x25 = x24.replace("ئ", "z");
                    x26 = x25.replace("ء", "x");
                    x27 = x26.replace("ؤ", "c");
                    x28 = x27.replace("ر", "v");
                    x29 = x28.replace("ى", "n");
                    x30 = x29.replace("ة", "m");
                    x31 = x30.replace("و", ",");
                    x32 = x31.replace("ز", ".");
                    x33 = x32.replace("ظ", "/");
                    x34 = x33.replace("ذ", "`");
                    x35 = x34.replace("ﻻ", "b");
                    helpPane.setText(x35);
                }
            }
        });


        frame.add(panel);
        frame.setSize(500, 250);

        frame.setLocationRelativeTo(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }



}
