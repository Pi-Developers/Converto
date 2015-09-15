# -*- coding: utf-8 -*-
#!/usr/bin/python3


#author @mohamed rashad


import sys
from Converto import *
from gi.repository import Gtk, Gdk

class ConvertoGUI(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Converto", border_width=10)
        self.connect("delete-event", Gtk.main_quit)
        self.clipboard=Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.vbox=Gtk.Box(spacing=6, orientation=Gtk.Orientation.VERTICAL)
        self.hbox=Gtk.Box(spacing=6, orientation=Gtk.Orientation.HORIZONTAL)
        self.convertButton=Gtk.Button("Convert")
        self.convertButton.connect("clicked", self.convertButtonClicked)
        self.copyButton=Gtk.Button("Copy")
        self.copyButton.connect("clicked", self.copyButtonClicked)
        self.entry=Gtk.Entry()
        self.vbox.pack_start(self.entry, True, True, 0)
        self.vbox.pack_start(self.hbox, True, True, 0)
        self.hbox.pack_start(self.convertButton, True, True, 0)
        self.hbox.pack_start(self.copyButton, True, True, 0)
        self.add(self.vbox)
        self.show_all()

    def convertButtonClicked (self, button):
        convert=Converto().convert
        self.entry.set_text(convert(self.entry.get_text()))

    def copyButtonClicked (self, button):
        self.clipboard.set_text(self.entry.get_text(), -1)
    
if __name__ == "__main__":
    ConvertoGUI()
    Gtk.main()