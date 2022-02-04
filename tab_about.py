from tkinter import Frame, StringVar
from tkinter.ttk import Style, Label, Entry, Button

from components.ScrollableFrame import ScrollableFrame

import functions

class AboutTab(Frame):
    text_input = None
    file_contents = ''
    text_file = None

    def __init__(self):
        super().__init__()

        self.master.title('About')

        # Lisame stiili
        self.styles = Style(self)
        self.styles.configure('about.TLabel', font=10, color='red', wraplength=300)

        # See rida on kõige viimane __init__()
        self.pack()

    def drawTab(self):
        text = Label(
            self,
            text='See rakendus on näidiseks, kuidas komponente siin kasutada!',
            style='about.TLabel'
        )
        text.pack()


        text_label = Label(self, text='Kirjuta tekst:')
        text_label.pack()
        self.text_input = Entry(self, width=70)
        self.text_input.pack()

        name_label = Label(self, text='Kirjuta nimi:')
        name_label.pack()
        self.name_input = Entry(self, width=70)
        self.name_input.pack()

        button = Button(self, text="Salvesta faili", cursor="hand2", command=self.save_to_file)
        button.pack()

        self.file_contents = StringVar()
        self.append_to_textfile_content()

        scrollable_area = ScrollableFrame(self)
        scrollable_area.pack()
        self.scrollable_area = scrollable_area

        self.text_file = Label(self.scrollable_area, background="green", textvariable=self.file_contents)
        self.text_file.pack()

    def save_to_file(self):
        text = self.text_input.get()
        name = self.name_input.get()

        content = { 'name': name, 'text': text }

        functions.write_to_csv('log.csv', content)
        print(functions.read_csv('log.csv')) # prindime csv listi välja
        # self.append_to_textfile_content()

    def append_to_textfile_content(self):
        text = functions.read_file('log.txt')
        self.file_contents.set("".join(text))


