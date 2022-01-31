from tkinter import ttk
from tkinter import Tk, Frame, Label

window = Tk()
window.title('New Project')

window.iconbitmap('./mario.ico') # pilt peab .ico formaadis

window.geometry('640x480')


# põhi kood
tabs_group = ttk.Notebook(window)
tabs_group.pack(fill='both', expand=1)

# Loome tabid
main_tab = Frame(tabs_group)
main_tab.pack()

about_tab = Frame(tabs_group)
about_tab.pack()

# Lisame tabid tabide gruppi
tabs_group.add(main_tab, text="Main")
tabs_group.add(about_tab, text="About Us")


# Loome tabidele sisu
# Main
Label(main_tab, text="Siin on põhiline info").grid(
    column=0, row=0, padx=20, pady=20)


window.mainloop()
