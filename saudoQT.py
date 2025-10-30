import sys
import SegundaFiestra

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout)


class NosaPrimeiraFiestra (QMainWindow):
    def __init__(self):
        super().__init__()

        self.segundaFiestra = None
        self.nomeOculto = ""
        self.setWindowTitle("A miña primeira fiestra con QT")
        self.setMinimumSize(500, 300)

        """
        self.txtSaudo = QLineEdit()
        self.lblEtiqueta = QLabel("Ola a todos")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter |Qt.AlignmentFlag.AlignVCenter)
        """

        caixaV = QVBoxLayout()

        self.lblEtiqueta = QLabel("OLA A TODOS!")
        self.lblEtiqueta.setText("OLA A TODOS E TODAS!")

        self.txtSaudo = QLineEdit()
        self.txtSaudo.setPlaceholderText("INTRODUCE O TEU NOME")
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)
        self.txtSaudo.textChanged.connect(self.on_btnSaudo_textChanged)

        btnSaudo = QPushButton ("Saúdo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        """ Mudamos btnMaiusculas por chkMaiusculas
        self.btnMaiusculas = QPushButton("Maiúsculas")
        self.btnMaiusculas.setCheckable(True)
        self.btnMaiusculas.setChecked(True)
        self.btnMaiusculas.toggled.connect(self.on_btnMaiusculas_toggled)
        """
        caixaH = QHBoxLayout()
        self.chkMaiusculas = QCheckBox("Maiúsculas")
        self.chkMaiusculas.setChecked(True)
        self.chkMaiusculas.toggled.connect(self.on_chkMaiusculas_toggled)
        self.maiusculas = True

        self.chkOculto = QCheckBox ("Oculto")
        self.chkOculto.toggled.connect (self.on_chkOculto_toggled)
        caixaH.addWidget(self.chkMaiusculas)
        caixaH.addWidget(self.chkOculto)

        btnSegundaFiestra = QPushButton("Segunda fiestra")
        btnSegundaFiestra.clicked.connect(self.on_btnSegundaFiestra_clicked)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        #caixaV.addWidget(self.btnMaiusculas)
        #caixaV.addWidget(self.chkMaiusculas)
        caixaV.addLayout(caixaH)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnSegundaFiestra)

        container = QWidget()
        container.setLayout(caixaV)

        self.setCentralWidget(container)
        self.show()

    def on_btnSaudo_clicked (self):
        if self.chkOculto.isChecked():
            nome = self.nomeOculto
        else:
            nome = self.txtSaudo.text()
        nome = nome.strip()
        if len(nome) != 0 :
            self.txtSaudo.clear()
            #self.txtSaudo.setText("")
            self.lblEtiqueta.setText("Ola, " + nome + ". Encantado/a de coñecerte.")
        else:
            self.lblEtiqueta.setText("Introduce o teu nome para recibir un saúdo personalizado")
        self.on_btnMaiusculas_toggled()
        self.nomeOculto = ''
        self.txtSaudo.setText('')

    def on_btnSegundaFiestra_clicked(self):
        self.hide()
        if self.segundaFiestra is None:
            self.segundaFiestra = SegundaFiestra.SegundaFiestra(self)
            print("Creando a segunda fiestra")
        self.segundaFiestra.show()
        print("Ocultando o pai no pai")

    def on_btnMaiusculas_toggled (self):
        if self.chkMaiusculas.isChecked() :
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.maiusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.maiusculas = False

    def on_chkMaiusculas_toggled (self):
        if self.chkMaiusculas.isChecked() :
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.txtSaudo.setText (self.txtSaudo.text().upper())
            self.maiusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.txtSaudo.setText (self.txtSaudo.text().lower())
            self.maiusculas = False

    def on_chkOculto_toggled (self):
        if self.chkOculto.isChecked():
            self.nomeOculto = self.txtSaudo.text()
            self.txtSaudo.setText('*' * len(self.nomeOculto))
        else:
            self.txtSaudo.setText(self.nomeOculto)
            self.nomeOculto = ''

    def on_btnSaudo_textChanged(self):
        if self.maiusculas:
            self.txtSaudo.setText(self.txtSaudo.text().upper())
        else:
            self.txtSaudo.setText(self.txtSaudo.text().lower())
        nome = self.txtSaudo.text()
        if self.chkOculto.isChecked():
            for i, caracter in enumerate(nome):
                if caracter != '*':
                    if len(self.nomeOculto) == i:
                        self.nomeOculto = self.nomeOculto + caracter
                        break
                    else:
                        self.nomeOculto = self.nomeOculto [:i] + caracter + self.nomeOculto[i+1:]
            self.txtSaudo.setText('*'* len(self.nomeOculto))


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = NosaPrimeiraFiestra()
    aplicacion.exec()