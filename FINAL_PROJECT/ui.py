from PyQt6.QtGui import QIcon,QFont
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton,QLabel
import sys
from logic import Counter
class Clicker(QWidget):
    def __init__(self):
        super().__init__()

        self.stats = Counter()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CLICKER")

        self.button1 = QPushButton(self)
        self.button1.setIcon(QIcon("Coin_video_game.png"))
        self.button1.setIconSize(QSize(300, 300))
        self.button1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button1.resize(300,300)
        self.button1.clicked.connect(self.on_click)
        self.button1.move(300, 50)

        self.button2 = QPushButton(f"Upgrade cost:{self.stats.upgrade_cost}", self)
        self.button2.clicked.connect(self.more_m)
        self.button2.move(350, 400)
        self.button2.setCursor(Qt.CursorShape.PointingHandCursor)
        self.button2.resize(170,50)

        self.resize(900, 600)

        self.label_count = QLabel("Coins", self)
        self.label_count.move(390, 360)
        self.label_count.setFont(QFont("Arial", 20))
        self.label_count.resize(200, 40)

        self.label_info = QLabel("", self)
        self.label_info.move(80, 480)
        self.label_info.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.label_info.resize(700, 40)
        self.label_info.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_click(self):

        self.count=self.stats.increment()
        self.label_count.setText(f"Coins:{str(self.count)}")

    def more_m(self):
        success=self.stats.upgrade_coin()
        if success:
            self.label_count.setText(f"Coins: {self.stats.count}")
            self.button2.setText(f"Upgrade (Cost: {self.stats.upgrade_cost})")
            self.label_info.setStyleSheet("color: green;")
            self.label_info.setText(f"Upgraded! Click power increased to: {self.stats.click_power}")
        else:
            self.label_info.setStyleSheet("color: red;")
            self.label_info.setText("Not enough coins!")
