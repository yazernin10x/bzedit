from __future__ import annotations

from tkinter import Event, Tk
from tkinter.ttk import Button, Frame
from typing import Any, Type

from src.bzedit.config import IMAGE_DIR
from src.frontend.frame import TextArea
from src.frontend.utils import set_icon
from src.backend.command import Invoker, Cut, Copy, Paste, Delete, Undo, Redo, Save


class Toolbar(Frame):
    def __init__(self, parent: Tk, editor: TextArea) -> None:
        super().__init__(parent)
        self._parent = parent

        self._editor = editor
        self._editor.text_widget.bind("<ButtonRelease-1>", self.on_text_selection)
        self._editor.text_widget.bind("<KeyPress>", self.on_text_is_empty, "+")

        icon_open = set_icon(IMAGE_DIR / "open.png")
        self._open = Button(
            self,
            text="Ouvrir",
            command=self.open_file,
            image=icon_open,
            compound="left",
        )
        self._open.image = icon_open
        self._open.pack(side="left", padx=5, pady=5)
        self._parent.bind("<Control-o>", lambda event: self._open.invoke())

        icon_save = set_icon(IMAGE_DIR / "save.png")
        self._save = Button(
            self,
            text="Sauvegarder",
            command=self.save_file,
            state="disabled",
            image=icon_save,
            compound="left",
        )
        self._save.image = icon_save
        self._save.pack(side="left", padx=5, pady=5)
        self._parent.bind("<Control-s>", lambda event: self._save.invoke())

        icon_cut = set_icon(IMAGE_DIR / "cut.png")
        self._cut = Button(
            self,
            text="Couper",
            command=self.cut,
            state="disabled",
            image=icon_cut,
            compound="left",
            # style="Custom.TButton",
        )
        self._cut.image = icon_cut
        self._cut.pack(side="left", padx=5, pady=5)

        self._parent.bind("<Control-x>", lambda event: self._cut.invoke())
        # self._parent.bind("<Control-x>", self.shortcut)

        icon_copy = set_icon(IMAGE_DIR / "copy.png")
        self._copy = Button(
            self,
            text="Copier",
            command=self.copy,
            state="disabled",
            image=icon_copy,
            compound="left",
        )
        self._copy.image = icon_copy
        self._copy.pack(side="left", padx=5, pady=5)

        icon_paste = set_icon(IMAGE_DIR / "paste.png")
        self._paste = Button(
            self,
            text="Coller",
            command=self.paste,
            state="disabled",
            image=icon_paste,
            compound="left",
        )
        self._paste.image = icon_paste
        self._paste.pack(side="left", padx=5, pady=5)

        icon_delete = set_icon(IMAGE_DIR / "delete.png")
        self._delete = Button(
            self,
            text="Supprimer",
            command=self.delete,
            state="disabled",
            image=icon_delete,
            compound="left",
        )
        self._delete.image = icon_delete
        self._delete.pack(side="left", padx=5, pady=5)

        icon_undo = set_icon(IMAGE_DIR / "undo.png")
        self._undo = Button(
            self,
            text="Annuler",
            command=self.undo,
            state="disabled",
            image=icon_undo,
            compound="left",
        )
        self._undo.image = icon_undo
        self._undo.pack(side="left", padx=5, pady=5)
        self._editor.master.bind(
            "<<post-save>>", lambda event: self._undo.config(state="normal")
        )
        self._editor.master.bind(
            "<<post-load>>", lambda event: self._undo.config(state="normal")
        )

        icon_redo = set_icon(IMAGE_DIR / "redo.png")
        self._redo = Button(
            self,
            text="Refaire",
            command=self.redo,
            state="disabled",
            image=icon_redo,
            compound="left",
        )
        self._redo.image = icon_redo
        self._redo.pack(side="left", padx=5, pady=5)

        # Lier la fermeture de la fenêtre à la méthode save_text
        # self._parent.protocol("WM_DELETE_WINDOW", self._save.invoke())

    # def shortcut(self, event: Event) -> None:
    #     if event.state & 0x04 and event.keysym.lower() == "x":
    #         print("Control + X a été pressé !")
    #         self._cut.invoke()

    @property
    def editor(self) -> TextArea:
        """Associe l'éditeur à la barre d'outils."""
        return self._editor

    @editor.setter
    def editor(self, editor: TextArea) -> None:
        self._editor = editor

    def _check_selection(self) -> None:
        """Active ou désactive le bouton selon l'état de la sélection."""
        if self._editor.text_widget.tag_ranges("sel"):
            self._cut.config(state="normal")
            self._copy.config(state="normal")
            self._delete.config(state="normal")
        else:
            self._cut.config(state="disabled")
            self._copy.config(state="disabled")
            self._delete.config(state="disabled")

    def on_text_selection(self, event: Event) -> None:
        """Vérifie la sélection à chaque modification."""
        self._check_selection()

    def _active_save_button(self) -> None:
        if self._editor.is_empty():
            self._save.config(state="disabled")
        else:
            self._save.config(state="normal")

    def on_text_is_empty(self, event: Event) -> None:
        self._active_save_button()

    def cut(self) -> None:
        """Coupe le texte sélectionné."""
        self._invoke(Cut)
        self._paste.config(state="normal")
        self._editor.save()
        self._active_save_button()

    def copy(self) -> None:
        """Copie le texte sélectionné."""
        self._invoke(Copy)
        self._paste.config(state="normal")

    def paste(self) -> None:
        """Colle le texte depuis le presse-papiers."""
        # Sauveader le memento
        self._invoke(Paste)
        save = Save(self._editor.engine, self._editor.caretaker)
        Invoker.invoke(save)

    def delete(self) -> None:
        """Supprimé le texte sélectionné."""
        self._invoke(Delete)
        self._editor.save()
        self._active_save_button()

    def undo(self) -> None:
        """Annule la dernière action."""
        Invoker.invoke(
            Undo(
                self._editor.engine,
                self._editor.caretaker,
            )
        )

        if self._editor.text == self._editor.engine.buffer:
            Invoker.invoke(
                Undo(
                    self._editor.engine,
                    self._editor.caretaker,
                )
            )

        self._editor.text = self._editor.engine.buffer
        self._redo.config(state="normal")
        if not self._editor.engine.buffer:
            self._undo.config(state="disabled")

        self._editor.save()
        self._active_save_button()

    def redo(self) -> None:
        """Refait la dernière action annulée."""
        Invoker.invoke(
            Redo(
                self._editor.engine,
                self._editor.caretaker,
            )
        )
        self._editor.text = self._editor.engine.buffer
        if not self._editor.caretaker.is_redo():
            self._redo.config(state="disabled")

    def _invoke(self, class_name: Type[Any]) -> None:
        print(self._editor.start, self._editor.end)
        Invoker.invoke(
            class_name(
                self._editor.engine,
                self._editor.start,
                self._editor.end,
            )
        )
        self._editor.text = self._editor.engine.buffer
        print("--------------------------------------")
        print(self._editor.start, self._editor.end)
        print(self._editor.engine.buffer)
        print(self._editor.engine.clipboard)

    def open_file(self) -> None:
        """Ouvre un fichier et insère son contenu."""
        self._editor.open_file()
        self._save.config(state="normal")

    def save_file(self) -> None:
        """Sauvegarde le contenu dans un fichier."""
        self._editor.save_file()
        self._save.config(state="disabled")
