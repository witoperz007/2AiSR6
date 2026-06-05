from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

class ButtonApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("CLICKER")
        self.button1 = QPushButton("CLICK TO EARN MONEY", self)
        self.button2 = QPushButton("Upgrade", self)
        self.button1.clicked.connect(self.on_click)
        self.button1.move(60, 50)
        self.button2.clicked.connect(self.more_m)
        self.button2.move(80, 120)
        self.resize(300, 200)
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