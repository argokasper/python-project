from tkinter import Frame, StringVar
from tkinter.ttk import Style, Label, Entry, Button

from components.Table import Table

import functions

class AboutTab(Frame):
    text_input = None
    file_contents = ''
    # text_file = None

    data_table = None
    data_file_name = 'messages.csv'

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

        self.input_value = StringVar()
        self.input_value.trace_add('write', self.on_input)
        self.filter_input = Entry(self, textvariable=self.input_value)
        self.filter_input.pack()

        self.messages = self.original_messages = functions.read_csv(self.data_file_name)
        self.data_table = Table(self, data = self.messages, headers = ['Nimi', 'Sõnum'])
        self.data_table.pack()

    def save_to_file(self):
        text = self.text_input.get()
        name = self.name_input.get()

        content = { 'name': name, 'text': text }

        functions.write_to_csv(self.data_file_name, content)
        self.original_messages = functions.read_csv(self.data_file_name) # kirjuta alati värske faili sisu original_messages muutujasse
        self.data_table.append_row(content)

    def append_to_textfile_content(self):
        text = functions.read_file('log.txt')
        self.file_contents.set("".join(text))

    def on_input(self, *args):
        term = self.input_value.get()
        self.filter_scores(term)
        self.data_table.update(self.messages)

    def filter_scores(self, search):
        if search == '':
            self.messages = self.original_messages
        else:
            if len(self.messages) == 0:
                self.messages = self.original_messages

            filtered_scores = list(filter(self.filter, self.messages))
            self.messages = filtered_scores

    def filter(self, score_line):
        search = self.input_value.get()
        return search.lower() in score_line['name'].lower() or search.lower() in score_line['text'].lower()



