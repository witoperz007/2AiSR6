from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QSize, Qt, QPropertyAnimation, QPoint, QSequentialAnimationGroup
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGraphicsOpacityEffect
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

        self.show_floating_text()

    def show_floating_text(self):

        mouse_pos = self.mapFromGlobal(self.cursor().pos())

        float_label = QLabel(f"+{self.stats.click_power}", self)
        float_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        float_label.setStyleSheet("color: #FFD700;")
        float_label.resize(50, 30)

        float_label.move(mouse_pos.x() - 10, mouse_pos.y() - 20)
        float_label.show()

        anim_move = QPropertyAnimation(float_label, b"pos")
        anim_move.setDuration(600)
        anim_move.setStartValue(float_label.pos())
        anim_move.setEndValue(QPoint(float_label.x(), float_label.y() - 60))

        opacity_effect = QGraphicsOpacityEffect(float_label)
        float_label.setGraphicsEffect(opacity_effect)

        anim_fade = QPropertyAnimation(opacity_effect, b"opacity")
        anim_fade.setDuration(600)
        anim_fade.setStartValue(1.0)
        anim_fade.setEndValue(0.0)

        anim_move.start()
        anim_fade.start()

        anim_move.finished.connect(float_label.deleteLater)

        float_label.anim1 = anim_move
        float_label.anim2 = anim_fade

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
