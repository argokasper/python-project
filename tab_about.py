from tkinter import Frame
from tkinter.ttk import Style, Label

class AboutTab(Frame):
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
