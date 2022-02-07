from tkinter import Scrollbar, TOP, HORIZONTAL, VERTICAL, RIGHT, Y, BOTTOM, X, W, NO
from tkinter.ttk import Frame, Treeview

class Table(Frame):
    order = 'desc'

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

        # händlime treeview klikke
        self.tree.bind('<Button-1>', self.mouse_click)

    def update(self, data):
        # Kustutame kõik read ära, et kuvada värsket faili seisu (Ei ole hea lahendus, loome koos parema)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for row in data:
            self.tree.insert("", 0, values=tuple(row.values()))

    def append_row(self, row):
        self.tree.insert("", 0, values=tuple(row.values()))

    def sort(self, column, order = 'asc'):
        rows = [(self.tree.set(k, column), k) for k in self.tree.get_children()]
        rows.sort(reverse=(order != 'asc'))

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(rows):
            self.tree.move(k, '', index)

    def mouse_click(self, event):
        col = self.tree.identify_column(event.x)
        region = self.tree.identify_region(event.x, event.y)

        if region == 'heading' and (col == '#1' or  col == '#2'):
            if self.order == 'asc':
                self.order = 'desc'
            else:
                self.order = 'asc'

            self.sort(col, self.order)
