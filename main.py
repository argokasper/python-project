from tkinter.ttk import Notebook
from tkinter import Tk

from tab_main import MainTab
from tab_about import AboutTab

class App(Tk):
    def __init__(self):
        super().__init__()

        # Nüüd hakkame lisama aknale pealkirju ja ikoone
        # jm rakendust iseloomustavaid omadusi
        self.title('Minu Programm')
        self.iconbitmap('./mario.ico') # pilt peab .ico formaadis
        self.geometry('640x480')

        # Joonistame tab'ide grupi
        self.draw_tabs()


    def draw_tabs(self):
        # Loome tabide grupi
        tabs_group = Notebook(self)
        tabs_group.pack(fill='both', expand=1)

        #---------MAIN TAB---------
        # Loome main tab'i
        main_tab = MainTab()
        main_tab.drawTab()

        # Lisame loodud tab'i gruppi
        tabs_group.add(main_tab, text='Main')
        #--------MAIN TAB lõpp-------

        #---------ABOUT TAB---------
        # Loome main tab'i
        about_tab = AboutTab()
        about_tab.drawTab()

        # Lisame loodud tab'i gruppi
        tabs_group.add(about_tab, text='About')
        #--------ABOUT TAB lõpp-------

        # Siia võib juurde lisada uusi tab'e
        # analoogselt MainTab'ile ja AboutTab'ile



# Järgnev if lause kontrollib kas antud fail kutsutakse otse välja
# rohkem infot siin: https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
    app = App()
    app.mainloop()
