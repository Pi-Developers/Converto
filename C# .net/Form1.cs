/// <summary>
/// Converto Version 1.00
/// Coded By : Pi Developers
/// www.pi-developers.com
/// This Application is licensed under the terms of the GNU General Public License Ver. 3.00
/// </summary>


using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using System.IO;
using Microsoft.Win32;
using System.Diagnostics;

namespace Converto
{

    public partial class Form1 : Form
    {
        RegistryKey startup = Registry.CurrentUser.OpenSubKey("Software\\Microsoft\\Windows\\CurrentVersion\\Run", true);
        bool exit=false;
        [DllImport("user32.dll")]
        public static extern ushort GetAsyncKeyState(int Key);
        public Form1()
        {
            InitializeComponent();
        }
      
        public static bool IsPushed(System.Windows.Forms.Keys hKey)
        {

            return 0 != (GetAsyncKeyState((int)hKey) & 0x8000);

        }

        void convert()
        {
            try
            {
                string temp = Clipboard.GetText();
                SendKeys.Send("^(a)");
                SendKeys.Send("^(c)");
                string x = Clipboard.GetText();
                x = x.ToLower();
                string y;

                if (x.Contains("a") ||
                    x.Contains("b") ||
                    x.Contains("c") ||
                    x.Contains("d") ||
                    x.Contains("e") ||
                    x.Contains("f") ||
                    x.Contains("g") ||
                    x.Contains("h") ||
                    x.Contains("i") ||
                    x.Contains("j") ||
                    x.Contains("k") ||
                    x.Contains("l") ||
                    x.Contains("m") ||
                    x.Contains("n") ||
                    x.Contains("o") ||
                    x.Contains("p") ||
                    x.Contains("q") ||
                    x.Contains("r") ||
                    x.Contains("s") ||
                    x.Contains("t") ||
                    x.Contains("u") ||
                    x.Contains("v") ||
                    x.Contains("w") ||
                    x.Contains("x") ||
                    x.Contains("y") ||
                    x.Contains("z"))
                {

                    y = x.Replace("q", "ض").
                        Replace("w", "ص").
                        Replace("e", "ث").
                        Replace("r", "ق").
                        Replace("t", "ف").
                        Replace("y", "غ").
                        Replace("u", "ع").
                        Replace("i", "ه").
                        Replace("o", "خ").
                        Replace("p", "ح").
                        Replace("[", "ج").
                        Replace("]", "د").
                        Replace("a", "ش").
                        Replace("s", "س").
                        Replace("d", "ي").
                        Replace("f", "ب").
                        Replace("g", "ل").
                        Replace("h", "ا").
                        Replace("j", "ت").
                        Replace("l", "م").
                        Replace(";", "ك").
                        Replace("'", "ط").
                        Replace("k", "ن").
                        Replace("z", "ئ").
                        Replace("x", "ء").
                        Replace("c", "ؤ").
                        Replace("v", "ر").
                        Replace("b", "لا").
                        Replace("n", "ى").
                        Replace("m", "ة").
                        Replace(",", "و").
                        Replace(".", "ز").
                        Replace("/", "ظ").
                        Replace("`", "ذ");

                    Clipboard.SetText(y);
                    SendKeys.Send("^(v)");
                    Clipboard.SetText(temp);

                }

                else if (x.Contains("ض") ||
                    x.Contains("ص") ||
                    x.Contains("ث") ||
                    x.Contains("ق") ||
                    x.Contains("ف") ||
                    x.Contains("غ") ||
                    x.Contains("ع") ||
                    x.Contains("ه") ||
                    x.Contains("خ") ||
                    x.Contains("ح") ||
                    x.Contains("ج") ||
                    x.Contains("د") ||
                    x.Contains("ش") ||
                    x.Contains("س") ||
                    x.Contains("ي") ||
                    x.Contains("ب") ||
                    x.Contains("ل") ||
                    x.Contains("ا") ||
                    x.Contains("ت") ||
                    x.Contains("ن") ||
                    x.Contains("م") ||
                    x.Contains("ك") ||
                    x.Contains("ط") ||
                    x.Contains("ئ") ||
                    x.Contains("ء") ||
                    x.Contains("ر") ||
                    x.Contains("لا") ||
                    x.Contains("ى") ||
                    x.Contains("ة") ||
                    x.Contains("ز") ||
                    x.Contains("ظ") ||
                    x.Contains("ؤ") ||
                    x.Contains("و"))
                {
                    y = x.Replace("ض", "q")
                        .Replace("ص", "w")
                        .Replace("ث", "e")
                        .Replace("ق", "r")
                        .Replace("ف", "t")
                        .Replace("غ", "y")
                        .Replace("ع", "u")
                        .Replace("ه", "i")
                        .Replace("خ", "o")
                        .Replace("ح", "p")
                        .Replace("ج", "[")
                        .Replace("د", "]")
                        .Replace("ش", "a")
                        .Replace("س", "s")
                        .Replace("ي", "d")
                        .Replace("ب", "f")
                        .Replace("ل", "g")
                        .Replace("ا", "h")
                        .Replace("ت", "j")
                        .Replace("ن", "k")
                        .Replace("م", "l")
                        .Replace("ك", ";")
                        .Replace("ط", "'")
                        .Replace("ئ", "z")
                        .Replace("ء", "x")
                        .Replace("ؤ", "c")
                        .Replace("ر", "v")
                        .Replace("لا", "b")
                        .Replace("ى", "n")
                        .Replace("ة", "m")
                        .Replace("و", ",")
                        .Replace("ز", ".")
                        .Replace("ظ", "/")
                        .Replace("ذ", "`");
                    Clipboard.SetText(y);
                    SendKeys.Send("^(v)");
                    Clipboard.SetText(temp);
                }
            }
            catch (Exception)
            { 
            
            }

        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
            radioButton1.Checked = Properties.Settings.Default.Hidden;
            
            comboBox1.SelectedIndex = 2;
            checkBox1.Checked = Properties.Settings.Default.Startup;
            comboBox1.SelectedIndex = Properties.Settings.Default.Hotkey;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            notifyIcon1.Icon = Properties.Resources.icon;
            if (checkBox1.Checked == true)
            {
                startup.SetValue("Converto", Application.StartupPath.ToString()+"\\"+System.Reflection.Assembly.GetExecutingAssembly().GetName().Name+".exe");
                Properties.Settings.Default.Startup = true;

            }
            else if (checkBox1.Checked == false)
            {
                startup.DeleteValue("Converto", false);
                Properties.Settings.Default.Startup = false;
            }


            if (this.Visible == false)
            {
                showToolStripMenuItem.Text = "Show";
            }
            else
            {
                showToolStripMenuItem.Text = "Hide";
            }
            
            char shk = comboBox1.Text[0];
            int z = (int)(shk);
            string cc = z.ToString();

            if (checkBox2.Checked)
            {
                if (IsPushed(Keys.ControlKey) && IsPushed((Keys)Int32.Parse(z.ToString())))
                {
                    convert();
                
                }
 
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox2.Checked==false)
            {
                checkBox2.Checked=true;
            }
            else
            {
                checkBox2.Checked=true;
            }
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                this.Hide();
                notifyIcon1.Icon = SystemIcons.Application;
                notifyIcon1.BalloonTipText = "Converto is here";
                notifyIcon1.ShowBalloonTip(1000);
            }
        }

        private void notifyIcon1_DoubleClick(object sender, EventArgs e)
        {
            this.Show();
            this.WindowState = FormWindowState.Normal;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
            this.Hide();
            
            notifyIcon1.Icon = SystemIcons.Application;
            notifyIcon1.BalloonTipText = "Converto is here";
            notifyIcon1.ShowBalloonTip(100);
        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.Show();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            button2_Click(sender, e);
            if (exit == true)
            {
                

                e.Cancel = false;
                
            }
            else
            {
                e.Cancel = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if(MessageBox.Show("Are you sure?","Exit",MessageBoxButtons.YesNo,MessageBoxIcon.Question)==DialogResult.No)
            {
                return;
            }
            exit = true;
            Properties.Settings.Default.Hidden = radioButton1.Checked;
            Properties.Settings.Default.Hotkey = comboBox1.SelectedIndex;
            Properties.Settings.Default.Save();
            Application.Exit();
        }

        private void showToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (this.Visible == false)
            {
                this.Show();
            }
            else
            {
                this.Hide();
            }
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            button1_Click(sender, e);
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            
        }

        private void Form1_Shown(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                this.Hide();
                button2_Click(sender, e);
            }
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
           
            try
            {
                Process.Start("http://www.pi-developers.com");
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            try
            {
                Process.Start("mailto:mmsmhh@gmail.com");
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

       
    }

}