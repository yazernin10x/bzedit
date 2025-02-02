from __future__ import annotations
from tkinter import Tk

from src.frontend.utils import set_icon
from src.frontend.frame import Toolbar, TextArea
from src.bzedit.config import APP_TITLE, APP_GEOMETRY, IMAGE_DIR


class App(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.icon_tk = set_icon(IMAGE_DIR / "icon.png")
        self.iconphoto(True, self.icon_tk)

        self.title(APP_TITLE)
        self.geometry(APP_GEOMETRY)
        dim = APP_GEOMETRY.split("x")
        self.minsize(int(dim[0]), int(dim[1]))
        self._center_window(self)  # Centre la fenêtre

        self._editor = TextArea(self)
        self._editor.pack(side="bottom", fill="both", expand=True)

        self._toolbar = Toolbar(self, self._editor)
        self._toolbar.pack(side="top", fill="x")

    def _center_window(self, window: Tk) -> None:
        """Centre la fenêtre sur l'écran."""
        window.update_idletasks()  # Met à jour les dimensions de la fenêtre
        width = window.winfo_width()  # Largeur de la fenêtre
        height = window.winfo_height()  # Hauteur de la fenêtre
        screen_width = window.winfo_screenwidth()  # Largeur de l'écran
        screen_height = window.winfo_screenheight()  # Hauteur de l'écran
        x = (screen_width - width) // 2  # Position horizontale
        y = (screen_height - height) // 2  # Position verticale
        window.geometry(f"{width}x{height}+{x}+{y}")  # Applique la position
