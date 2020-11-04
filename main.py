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

        self.entry = Gtk.Entry()
        self.entry.connect("changed", self.entry_changed)
        box.pack_start(self.entry, True, True, 0)

        self.result = Gtk.Entry()
        self.result.set_editable(False)
        box.pack_start(self.result, True, True, 0)

    def entry_changed(self, widget):
        input = self.entry.get_text()
        x = evaluate(input)
        if (x is not None):
            self.result.set_text(str(x))
        elif(input == ""):
            self.result.set_text("")
        else:
            self.result.set_text("syntax error")


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()