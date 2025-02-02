from __future__ import annotations

from tkinter import (
    SEL_FIRST,
    SEL_LAST,
    Event,
    TclError,
    Text,
    Tk,
    filedialog,
    messagebox,
)
from tkinter.ttk import Frame, Scrollbar

from src.backend.core import Engine
from backend.memento import Caretaker
from src.backend.command import Invoker, Insert, Save, Delete
from bzedit.config import DEFAULT_FILE_EXTENSION, SUPPORTED_FILE_TYPES


class TextArea(Frame):
    def __init__(self, parent: Tk) -> None:
        super().__init__(parent)
        self.pack(fill="both", expand=True)
        self._buffer = ""

        self._engine = Engine()
        self._caretaker = Caretaker()

        self._text = Text(self, wrap="word")
        self._text.grid(row=0, column=0, sticky="nsew")
        self._text.bind("<KeyPress>", self.on_key_press)

        self.v_scrollbar = Scrollbar(
            self, orient="vertical", command=self._text.yview("end")
        )
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")

        self.h_scrollbar = Scrollbar(
            self, orient="horizontal", command=self._text.xview
        )
        self.h_scrollbar.grid(row=1, column=0, sticky="ew")

        self._text.configure(
            yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.save()

    def remove_control_chars(self, text: str) -> str:
        return text.translate(
            str.maketrans(
                "", "", "".join(chr(i) for i in range(32) if i not in (10, 13))
            )
        )

    def on_key_press(self, event: Event) -> None:
        self.save()

        char = event.char
        if event.keysym == "Return":
            char = "\n"

        if event.keysym == "BackSpace":
            self._buffer = self.text
        else:
            self._buffer += char

        print("******************************")
        print(self._engine.buffer)
        print(self.text)
        print(self._buffer)
        print(event.keysym)
        if event.keysym in ("space", "Tab", "Return"):
            delete = Delete(self._engine, 0, self._engine.selection.buffer_end)
            Invoker.invoke(delete)
            Invoker.invoke(Insert(self._engine, self.text, 0, 0))
            Invoker.invoke(Save(self._engine, self._caretaker))
            self.master.event_generate("<<post-save>>")

    def cursor_pos(self) -> int:
        return int(self._text.index("insert").split(".")[1])

    @property
    def text_widget(self) -> Text:
        return self._text

    @property
    def engine(self) -> Engine:
        return self._engine

    @property
    def caretaker(self) -> Caretaker:
        return self._caretaker

    @property
    def text(self) -> str:
        """Retrieve the text content."""
        return self._text.get("1.0", "end-1c")

    @text.setter
    def text(self, text: str) -> None:
        self._buffer = text
        self._text.delete("1.0", "end")
        self._text.insert("1.0", text)

    @property
    def start(self) -> int:
        return self._get_column_selection()[0]

    @property
    def end(self) -> int:
        return self._get_column_selection()[1]

    def is_empty(self) -> bool:
        return not self.text.strip()

    def save(self) -> None:
        if self.is_empty():
            insert = Insert(self._engine, "", 0, 0)
            Invoker.invoke(insert)
            save = Save(self._engine, self._caretaker)
            Invoker.invoke(save)

    def _get_column_selection(self) -> tuple[int, int]:
        """Récupère les indices de colonnes de la sélection dans le widget Text."""
        try:
            start_index = self._text.index(SEL_FIRST)
            end_index = self._text.index(SEL_LAST)
        except TclError:
            index = int(self._text.index("insert").split(".")[1])
            start_index = end_index = f"{index}.{index}"
        finally:
            start_column = int(start_index.split(".")[1])
            end_column = int(end_index.split(".")[1])

        return start_column, end_column

    def _open_file_dialog(self) -> None:
        """Ouvre une fenêtre pour sélectionner un fichier et insère son contenu dans l'éditeur."""
        file_path = filedialog.askopenfilename(
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text = content
                    if content:
                        delete = Delete(
                            self._engine, 0, self._engine.selection.buffer_end
                        )
                        Invoker.invoke(delete)
                        Invoker.invoke(Insert(self._engine, content, 0, 0))
                        Invoker.invoke(Save(self._engine, self._caretaker))
                        self.master.event_generate("<<post-load>>")

            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier : {e}")

    def open_file(self) -> None:
        """Ouvre un fichier et insère son contenu."""
        if self.is_empty():
            self._open_file_dialog()
        else:
            save_response = messagebox.askyesnocancel(
                "Sauvegarder ?",
                "L'éditeur contient du texte. Souhaitez-vous sauvegarder avant d'ouvrir un nouveau fichier ?",
            )

            match save_response:
                case True:  # Oui
                    if self.save_file():
                        self._open_file_dialog()
                case False:  # Non
                    self._open_file_dialog()
                case None:  # Annuler
                    return

    def save_file(self) -> bool:
        """Ouvre une fenêtre pour sauvegarder le fichier."""
        file_path = filedialog.asksaveasfilename(
            defaultextension=DEFAULT_FILE_EXTENSION,
            filetypes=SUPPORTED_FILE_TYPES,
        )
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(self.text)
                return True  # Sauvegarde réussie
            except Exception as e:
                messagebox.showerror(
                    "Erreur", f"Impossible de sauvegarder le fichier : {e}"
                )
        return False
