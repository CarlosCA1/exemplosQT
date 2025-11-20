import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2025 grupo A")

        self.albaras = [['1111nm', '02/11/2024', '1111', 'Ana', 'Ruiz'],
                    ["2222io", "08/03/2024", "2222", "Pedro", "Diz"],
                    ["3333qw", "23/10/2025", "3333", "Rosa", "Sanz"]]

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.label_titulo = QLabel("Albará")
        main_layout.addWidget(self.label_titulo)

        h1 = QHBoxLayout(central_widget)
        self.label1 = QLabel("Número albará")
        self.cmbComboBox = QComboBox()
        self.label2 = QLabel("Data")
        self.texto1 = QLineEdit()
        h1.addWidget(self.label1)
        h1.addWidget(self.cmbComboBox)
        h1.addWidget(self.label2)
        h1.addWidget(self.texto1)
        main_layout.addLayout(h1)

        h2= QHBoxLayout(central_widget)
        self.label3 = QLabel("Número cliente")
        self.texto2 = QLineEdit()
        self.label4 = QLabel("Nome cliente")
        self.texto3 = QLineEdit()
        h1.addWidget(self.label3)
        h1.addWidget(self.texto2)
        h1.addWidget(self.label4)
        h1.addWidget(self.texto3)
        main_layout.addLayout(h2)

        h3 = QHBoxLayout(central_widget)
        self.label5 = QLabel("Apelidos")
        self.texto4 = QLineEdit()
        h1.addWidget(self.label5)
        h1.addWidget(self.texto4)
        main_layout.addLayout(h3)

        h4 = QHBoxLayout(central_widget)
        self.boton1 = QPushButton("Engadir")
        self.boton2 = QPushButton("Editar")
        self.boton3 = QPushButton("Borrar")
        h4.addWidget(self.boton1)
        h4.addWidget(self.boton2)
        h4.addWidget(self.boton3)
        main_layout.addLayout(h4)

        self.cadro_texto = QTextEdit()
        main_layout.addWidget(self.cadro_texto)

        h6 = QHBoxLayout(central_widget)
        self.boton4 = QPushButton("Cancelar")
        self.boton5 = QPushButton("Aceptar")
        h6.addWidget(self.boton4)
        h6.addWidget(self.boton5)
        main_layout.addLayout(h6)
'''
        gpbCliente = QGroupBox("Cliente")

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")

        txtNumeroCliente = QLineEdit()
        txtNomeCliente = QLineEdit()
        txtApelidosCliente = QLineEdit()
        txtDireccion = QLineEdit()
        txtCidade = QLineEdit()
        cmbProvincia = QComboBox()

        self.txeClientes = QTextEdit()

        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        
'''


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()