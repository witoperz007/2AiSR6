from PyQt6.QtWidgets import QApplication
from ui import ButtonApp
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonApp()
    window.show()
    sys.exit(app.exec())