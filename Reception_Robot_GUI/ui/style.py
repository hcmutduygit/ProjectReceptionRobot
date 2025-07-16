import os

def load_stylesheet(filename):
    full_path = os.path.join(os.path.dirname(__file__), filename)
    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

QMSGBOX_STYLE = load_stylesheet("style.qss")
