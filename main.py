#This file is part of lCalc which is released under the MIT License.
#See the file 'LICENSE' for full license details.

from eval import evaluate
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "lCalc")
        self.set_border_width(10)
        self.set_size_request(500, 300)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        self.entry_buffer = Gtk.TextBuffer()
        self.entry_buffer.connect("changed", self.entry_changed)
        self.tag = self.entry_buffer.create_tag("red_foreground", foreground="red")
        self.tag_set = False
        self.entry_textview = Gtk.TextView(buffer=self.entry_buffer)
        self.entry_textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        box.pack_start(self.entry_textview, True, True, 0)

        self.result_buffer = Gtk.TextBuffer()
        self.result_textview = Gtk.TextView(buffer=self.result_buffer)
        self.result_textview.set_editable(False)
        self.result_textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        box.pack_start(self.result_textview, True, True, 0)

    def entry_changed(self, widget):
        start_iter = self.entry_buffer.get_start_iter()
        end_iter = self.entry_buffer.get_end_iter()
        input = self.entry_buffer.get_text(start_iter, end_iter, True)

        if (self.tag_set):
            self.entry_buffer.remove_tag(self.tag, start_iter, end_iter)
            self.tag_set = False

        x = evaluate(input)
        if (x is not None):
            self.result_buffer.set_text(str(x))
        elif(input == ""):
            self.result_buffer.set_text("")
        else:
            self.entry_buffer.apply_tag(self.tag, start_iter, end_iter)
            self.tag_set = True
            self.result_buffer.set_text("")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
