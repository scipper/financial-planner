from tkinter import Tk, Menu, Frame, Label, Button, Entry
from tkinter.ttk import Combobox

from Dashboard.Dashboard import Dashboard


class EditableTable(Frame):
    def __init__(self, parent, rows=3, cols=2, headers=None, **kwargs):
        super().__init__(parent, **kwargs)

        self.cols = cols
        self.entries = []

        # Überschriften
        if headers:
            for c, text in enumerate(headers):
                lbl = Label(self, text=text, font=("Arial", 10, "bold"))
                lbl.grid(row=0, column=c, padx=2, pady=2, sticky="nsew")

        # Initialzeilen
        for _ in range(rows):
            self.add_row()

        # Grid skalierbar machen
        for c in range(cols):
            self.columnconfigure(c, weight=1)

    def add_row(self, values=None):
        """Eine neue Zeile hinzufügen"""
        r = len(self.entries) + 1  # +1 weil row=0 Überschriften sind
        row_entries = []
        for c in range(self.cols):
            e = Entry(self)
            e.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")
            if values and c < len(values):
                e.insert(0, values[c])
            else:
                e.insert(0, f"R{r}C{c+1}")
            row_entries.append(e)
        self.entries.append(row_entries)

        self.update_idletasks()  # Geometrie aktualisieren

    def get_data(self):
        """Alle Werte als Liste von Listen zurückgeben"""
        return [[e.get() for e in row] for row in self.entries]


class MiniWindow(Frame):
    def __init__(self, parent, title="Fenster", **kwargs):
        super().__init__(parent, relief="raised", borderwidth=2, **kwargs)

        self.config(width=400)
        self.pack_propagate(False)

        # Titelleiste
        titlebar = Frame(self)
        titlebar.pack(fill="x")

        lbl = Label(titlebar, text=title, font=("Arial", 10, "bold"))
        lbl.pack(side="left", padx=5)

        self.combo = Combobox(
            titlebar,
            values=["Option A", "Option B", "Option C"],
            state="readonly",
            width=10,
        )
        self.combo.current(0)
        self.combo.pack(side="right", padx=5)

        self.btn_data = Button(titlebar, text="Daten holen", command=self.on_button)
        self.btn_data.pack(side="right")

        # Tabelle
        self.table = EditableTable(self, rows=3, cols=2, headers=["Spalte 1", "Spalte 2"])
        self.table.pack(fill="x", padx=5, pady=5)

        # Button zum Hinzufügen von Zeilen
        self.btn_add = Button(self, text="+ Zeile hinzufügen", command=self.add_row)
        self.btn_add.pack(pady=(0, 5))

    def on_button(self):
        data = self.table.get_data()
        print(f"{self.combo.get()} -> {data}")

    def add_row(self):
        self.table.add_row()

class Gui:
    def __init__(self):
        self._root = Tk()
        self._root.state("zoomed")
        self._root.title("Financial Planner")
        frame = Frame(self._root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        mw1 = MiniWindow(frame, title="Income")
        mw1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        frame.rowconfigure((0,1), weight=1)
        frame.columnconfigure((0,1), weight=1)

        self._init_menu()

        self._dashboard = Dashboard()

    def _init_menu(self):
        self._menu = Menu(self._root)
        self._root.config(menu=self._menu)

        self._init_file_menu()
        self._init_category_menu()

    def _init_file_menu(self):
        self._file_menu = Menu(self._menu, tearoff=False)
        self._menu.add_cascade(label="File", menu=self._file_menu)
        self._file_menu.add_command(label="Exit", command=self._root.quit)

    def _init_category_menu(self):
        self._category_menu = Menu(self._menu, tearoff=False)
        self._menu.add_cascade(label="Category", menu=self._category_menu)
        self._category_menu.add_command(label="Add category", command=self._root.quit)

    def start(self):
        self._root.mainloop()


gui = Gui()
gui.start()