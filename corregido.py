import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QPushButton, QComboBox, QLineEdit, QGroupBox, QTextEdit, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt


class FiestraPrincipal2(QMainWindow):
    # Datos de los albaranes
    albaras = [['1111nm', '02/11/2024', '1111', 'Ana', 'Ruiz'],
               ['2222lo', '08/03/2024', '2222', 'Pedro', 'Diz'],
               ['3333qw', '23/10/2025', '3333', 'Rosa', 'Sanz']]

    def __init__(self):
        super().__init__()
        # Titulo de la ventana
        self.setWindowTitle("Exame 16-11-2025 grupo A")

        # GroupBox para datos del albarán
        dt_albaran = QGroupBox("Datos Albaran")

        # Labels y campos del formulario
        lblAlbaraTitulo = QLabel("Albará")
        lblData = QLabel("Data")
        self.txtData = QLineEdit()
        lblNumeroAlb = QLabel("Número de albará")
        self.cmbNumeroAlb = QComboBox()
        lblNumeroCliente = QLabel("Número Cliente")
        self.txtNumeroCliente = QLineEdit()
        lblNomeCliente = QLabel("Nome Cliente")
        self.txtNomeCliente = QLineEdit()
        lblApelidosCliente = QLabel("Apelidos")
        self.txtApelidosCliente = QLineEdit()

        # Área de texto para mostrar información
        self.txeClientes = QTextEdit()
        self.txeClientes.setReadOnly(True)

        # Botones de acción
        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        # Botones de control de ventana
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # Configuración inicial de botones
        btnAceptar.setEnabled(False)
        btnCancelar.clicked.connect(self.close)

        # Cargar datos en ComboBox
        for albaran in self.albaras:
            self.cmbNumeroAlb.addItem(albaran[0])

        # Conectar señales
        self.cmbNumeroAlb.currentIndexChanged.connect(self.cargarDatosAlbaran)
        btnEngadir.clicked.connect(self.escribirEnTextEdit)
        btnEditar.clicked.connect(self.on_btnEditar_clicked)

        # Cargar datos iniciales
        self.cargarDatosAlbaran(0)

        # GroupBox
        layoutGrid = QGridLayout()

        # Título Albará
        lblAlbaraTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lblAlbaraTitulo.setStyleSheet("font-weight: bold; font-size: 10pt; padding: 5px;")
        layoutGrid.addWidget(lblAlbaraTitulo, 0, 0, 1, 2)

        # Data
        layoutGrid.addWidget(lblData, 1, 0)
        layoutGrid.addWidget(self.txtData, 1, 1)

        #Número de albará
        layoutGrid.addWidget(lblNumeroAlb, 2, 0)
        layoutGrid.addWidget(self.cmbNumeroAlb, 2, 1)

        layoutGrid.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed), 3, 0, 1, 2)

        # Datos cliente
        layoutGrid.addWidget(lblNumeroCliente, 4, 0)
        layoutGrid.addWidget(self.txtNumeroCliente, 4, 1)
        layoutGrid.addWidget(lblNomeCliente, 5, 0)
        layoutGrid.addWidget(self.txtNomeCliente, 5, 1)
        layoutGrid.addWidget(lblApelidosCliente, 6, 0)
        layoutGrid.addWidget(self.txtApelidosCliente, 6, 1)

        dt_albaran.setLayout(layoutGrid)

        # Layout horizontal para botones de acción
        layoutBotonesAccion = QHBoxLayout()
        layoutBotonesAccion.addWidget(btnEngadir)
        layoutBotonesAccion.addWidget(btnEditar)
        layoutBotonesAccion.addWidget(btnBorrar)

        # Layout vertical superior
        layoutSuperior = QVBoxLayout()
        layoutSuperior.addWidget(dt_albaran)
        layoutSuperior.addLayout(layoutBotonesAccion)
        layoutSuperior.addWidget(self.txeClientes)

        # Layout horizontal para botones inferiores
        layoutBotonesInferiores = QHBoxLayout()
        layoutBotonesInferiores.addStretch(1)
        layoutBotonesInferiores.addWidget(btnCancelar)
        layoutBotonesInferiores.addWidget(btnAceptar)

        # Layout principal
        layoutPrincipal = QVBoxLayout()
        layoutPrincipal.addLayout(layoutSuperior)
        layoutPrincipal.addLayout(layoutBotonesInferiores)

        # Widget contenedor
        contenedor = QWidget()
        contenedor.setLayout(layoutPrincipal)
        self.setCentralWidget(contenedor)

        self.show()

    def cargarDatosAlbaran(self, index):
        # Carga los datos del albarán seleccionado
        if 0 <= index < len(self.albaras):
            datos_albaran = self.albaras[index]
            self.txtData.setText(datos_albaran[1])
            self.txtNumeroCliente.setText(datos_albaran[2])
            self.txtNomeCliente.setText(datos_albaran[3])
            self.txtApelidosCliente.setText(datos_albaran[4])

    def escribirEnTextEdit(self):
        # Escribe datos del cliente en el área de texto
        texto_num_cliente = self.txtNumeroCliente.text()
        elemento_num_albaran = self.cmbNumeroAlb.currentText()
        texto_a_añadir = f"Engadido - Cliente: {texto_num_cliente} | Albarán: {elemento_num_albaran}"
        self.txeClientes.append(texto_a_añadir)

    def on_btnEditar_clicked(self):
        # Recoge texto de QLineEdit y QComboBox y los incorpora en QTextEdit
        data = self.txtData.text()
        numero_albara = self.cmbNumeroAlb.currentText()
        numero_cliente = self.txtNumeroCliente.text()
        nome_cliente = self.txtNomeCliente.text()
        apelidos_cliente = self.txtApelidosCliente.text()

        # Crear línea de texto con todos los datos
        texto_editar = f"Editado - Data: {data} | Alb: {numero_albara} | Cliente: {numero_cliente} | Nome: {nome_cliente} | Apelidos: {apelidos_cliente}"

        # Añadir al QTextEdit
        self.txeClientes.append(texto_editar)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal2()
    sys.exit(aplicacion.exec())