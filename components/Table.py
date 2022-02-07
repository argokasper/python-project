from tkinter import Scrollbar, TOP, HORIZONTAL, VERTICAL, RIGHT, Y, BOTTOM, X, W, NO
from tkinter.ttk import Frame, Treeview

class Table(Frame):
    def __init__(self, container, data = [], headers = [], *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        margin = Frame(self, width=400)
        margin.pack(side=TOP)

        scrollbarx = Scrollbar(margin, orient=HORIZONTAL)
        scrollbary = Scrollbar(margin, orient=VERTICAL)
        self.tree = Treeview(margin, columns=headers, height=400, selectmode='extended',
            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        for i, header in enumerate(headers):
            self.tree.heading(header, text=header, anchor=W)
            self.tree.column('#{0}'.format(i), stretch=NO, minwidth=0, width=120)
        self.tree.pack()
        for row in data:
            self.tree.insert("", 0, values=tuple(row.values()))

    def update(self, data):
        # Kustutame kõik read ära, et kuvada värsket faili seisu (Ei ole hea lahendus, loome koos parema)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in data:
            self.tree.insert("", 0, values=tuple(row.values()))
