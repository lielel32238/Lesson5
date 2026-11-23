import sys

from PySide6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QSpinBox, QVBoxLayout, QWidget


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")

        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 10000)

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        controls = QHBoxLayout()
        controls.addWidget(self.spin_box)
        controls.addWidget(self.toggle_button)

        layout = QVBoxLayout(self)
        layout.addLayout(controls)

    def button_method(self, is_started: bool) -> None:
        self.toggle_button.setText("Stop" if is_started else "Start")


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
