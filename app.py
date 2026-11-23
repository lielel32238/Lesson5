import sys

from PySide6.QtWidgets import (
    QAbstractSpinBox,
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtCore import Qt, QTimer


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson 5")
        self.setMinimumWidth(200)

        self.counter = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_method)
        

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0, 10000)
        self.spinbox.setReadOnly(True)
        self.spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinbox.setStyleSheet("background-color: lightgray;")

        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setRange(0,255)
        self.slider.valueChanged.connect(self.slider_method)

        self.second_spinbox = QSpinBox()
        self.second_spinbox.setRange(0,255)
        self.second_spinbox.setReadOnly(True)
        self.second_spinbox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.second_spinbox.setStyleSheet("background-color: lightgray;")

        self.color_box = QLabel()
        self.color_box.setMinimumWidth(100)
        self.color_box.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.color_box.setStyleSheet('beckgtound-color: lightgray')

        self.toggle_button = QPushButton("Start")
        self.toggle_button.setCheckable(True)
        self.toggle_button.toggled.connect(self.button_method)

        controls = QHBoxLayout()
        controls.addWidget(self.spinbox)
        controls.addWidget(self.toggle_button)

        side_panel = QVBoxLayout()
        side_panel.addWidget(self.slider)
        side_panel.addWidget(self.second_spinbox)

        layout = QHBoxLayout(self)
        layout.addLayout(controls)
        layout.addLayout(side_panel)
        layout.addWidget(self.color_box)

    def button_method(self, is_started: bool) -> None:
        checked = self.toggle_button.isChecked()
        self.toggle_button.setText("Stop" if is_started else "Start")
        if checked:
            self.counter=0
            self.timer.start(10)
        else:
            self.timer.stop()

    def timer_method(self):
        self.counter +=1
        self.spinbox.setValue(self.counter)
        if self.counter == 500:
            self.timer.stop()

    def slider_method(self):
        value = self.slider.value()
        self.second_spinbox.setValue(value)
    


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
