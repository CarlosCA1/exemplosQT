import sys
import CaixaCor

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMainWindow, QApplication, QWidget

class ExemploBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con box")
        self.setMinimumSize(500, 300)
        caixaH = QHBoxLayout()
        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(CaixaCor.CaixaCor("blue"))
        caixaV1.addWidget(CaixaCor.CaixaCor("green"))
        caixaV1.addWidget(CaixaCor.CaixaCor("red"))
        caixaH.addLayout(caixaV1)

        caixaH.addWidget(CaixaCor.CaixaCor("yellow"))


        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(CaixaCor.CaixaCor("pink"))
        caixaV2.addWidget(CaixaCor.CaixaCor("grey"))
        caixaH.addLayout(caixaV2)

        widgetCentral = QWidget()
        widgetCentral.setLayout(caixaH)
        self.setCentralWidget(widgetCentral)
        
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = ExemploBox()
    aplicacion.exec()







