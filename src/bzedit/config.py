from pathlib import Path


BASE_DIR = ROOT_DIR = Path(__file__).resolve().parent.parent.parent
IMAGE_DIR = ROOT_DIR / "src" / "frontend" / "images"

# Application configurations
APP_TITLE = "BzEdit - Lightweight text editor"
APP_GEOMETRY = "870x700"

# File configurations
DEFAULT_FILE_EXTENSION = ".txt"
SUPPORTED_FILE_TYPES = [("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
