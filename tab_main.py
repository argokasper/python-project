from tkinter import Frame, Canvas, Text
# from tkinter import *
from tkinter.ttk import Style, Entry, Label, Button, Scrollbar

from components.ScrollableFrame import ScrollableFrame # Impordime custom komponendi scrollview loomiseks

class MainTab(Frame):
    pressed_keys = []
    scrollable_area = None
    scrollable_canvas = None

    def __init__(self):
        super().__init__()

        self.master.title('Main')

        # Lisame stiili
        self.styles = Style(self)
        self.styles.configure('main.TLabel', font=10, padding=10)
        self.styles.configure('TButton', background='green', font=14)
        self.styles.configure(
            'TEntry', background='green', padding='10 10 10 10')

        # Loome klahvi vajutuse tuvastaja
        self.bind_all('<Key>', self.key_pressed)

        self.pack()

    def drawTab(self):
        welcome_text = Label(
            self,
            text='Tere tulemast minu rakendusse!',
            style='main.TLabel'
        )
        welcome_text.pack()

        button = Button(self, text='Vajuta siia',
                        style='TButton', cursor='hand2')
        button.pack()

        text_input = Entry(self, width=50, style='TEntry')
        text_input.pack()

        delete = Button(self, text='Kustuta klahvivajutuste ajalugu', command=self.on_delete)
        delete.pack()

        scrollable_area = ScrollableFrame(self)
        scrollable_area.pack()
        self.scrollable_area = scrollable_area


    def key_pressed(self, event):
        key = Label(self.scrollable_area.scrollable_frame, text='Vajutasid: ' + event.keysym)
        self.pressed_keys.append(key)
        key.pack()

    def on_delete(self):
        for key_label in self.pressed_keys:
            key_label.destroy()

        self.pressed_keys.clear()

    def on_mousewheel(self, event):
        self.scrollable_canvas.yview_scroll(-1*(event.delta), 'units')
