import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)


class SegundaFiestra (QMainWindow):
    def __init__(self, fiestrapai):
        super().__init__()
        self.fiestrapai = fiestrapai
        self.setWindowTitle("Segunda fiestra con QT")
        self.setMinimumSize(500, 300)

        caixaV = QVBoxLayout()

        btnFiestraPai = QPushButton ("Fiestra pai")
        btnFiestraPai.clicked.connect(self.on_btnFiestraPai_clicked)

        caixaV.addWidget(btnFiestraPai)

        container = QWidget()
        container.setLayout(caixaV)

        self.setCentralWidget(container)
        self.show()

    def on_btnFiestraPai_clicked (self):
        if self. fiestrapai is not None:
            self.hide()
            print("Oculto a segunda fiestra")
            self.fiestrapai.show()
            print("Mostro o pai")
            self.destroy()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = SegundaFiestra(None)
    aplicacion.exec()