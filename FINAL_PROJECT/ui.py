from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class Clicker(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CLICKER")
        self.button1 = QPushButton(self)
        self.button1.setIcon(QIcon("Coin_video_game.png"))
        self.button1.setIconSize(QSize(300, 300))
        self.button1.resize(300,300)
        self.button2 = QPushButton("Upgrade", self)
        self.button1.clicked.connect(self.on_click)
        self.button1.move(300, 50)
        self.button2.clicked.connect(self.more_m)
        self.button2.move(350, 400)
        self.resize(900, 600)
        self.count = 0
        self.click_power=1

    def on_click(self):

        self.count=self.count+self.click_power
        print(self.count)
    def more_m(self):
        self.click_power=self.click_power+1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonApp()
    window.show()
    sys.exit(app.exec())