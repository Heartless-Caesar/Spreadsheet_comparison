from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QFileDialog, QDialog, QComboBox, QLineEdit, QMessageBox
from display_sheet import SecondWindow
from PyQt5 import uic
import webbrowser
import os


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Carrega o arquivo UI que será utilizado
        self.window = uic.loadUi("sheets.ui", self)

        # Carrega tela para alertas diversos
        self.message = QMessageBox()

        # Selecionar se os arquivos tem o mesmo numero de
        self.combobox = self.findChild(QComboBox, "comboBox")
        self.combobox.addItems(["Sim", "Não"])
        self.sw = None

        self.input = self.findChild(QLineEdit, "lineEdit")

        # Propriedades que irão ter o nome do arquivo para o pandas processar
        self.fname_one = ""
        self.fname_two = ""

        # Elementos do UI que serão manipulados de alguma forma
        self.select_file_one_button = self.findChild(
            QPushButton, "select_file_one_button")
        self.select_file_two_button = self.findChild(
            QPushButton, "select_file_two_button")
        self.execute_button = self.findChild(QPushButton, "execute_button")
        self.cancel_button = self.findChild(QPushButton, "cancel_button")

        # Label arquivo 1
        self.label_one = self.findChild(QLabel, "label")

        # Label arquivo 2
        self.label_two = self.findChild(QLabel, "label_2")

        # Opens dialog
        self.select_file_one_button.clicked.connect(self.open_file_dialog_one)
        self.select_file_two_button.clicked.connect(self.open_file_dialog_two)

        # Executa comparacao de planilhas
        self.execute_button.clicked.connect(self.open_second_window)

        self.help_button = self.findChild(QPushButton, "help_button")
        self.help_button.clicked.connect(self.open_help_window)

    def open_file_dialog_one(self):
        try:
            self.fname_one = QFileDialog.getOpenFileName(
                self, "Selecione um arquivo", "", "(*.xlsx);;(*.ods);;All Files (*)")

            if str(self.fname_one) != '':
                if str(self.fname_one).split("/")[-1].split("'")[0] != '(':
                    self.label_one.setText(
                        str(self.fname_one).split("/")[-1].split("'")[0])
        except FileNotFoundError as e:
            print("Escolha dois arquivos para realizar a comparação " + str(e))

    def open_file_dialog_two(self):
        try:
            self.fname_two = QFileDialog.getOpenFileName(
                self, "Selecione um arquivo", "", "(*.xlsx);;(*.ods);;All Files (*)")

            if str(self.fname_two) != '':
                if str(self.fname_two).split("/")[-1].split("'")[0] != '(':
                    self.label_two.setText(
                        str(self.fname_two).split("/")[-1].split("'")[0])
        except FileNotFoundError as e:
            print("Escolha dois arquivos para realizar a comparação " + str(e))

    def open_second_window(self):
        try:
            if str(self.fname_one).split("/")[-1].split("'")[0] and str(self.fname_two).split("/")[-1].split("'")[0] != "" or "(":
                self.sw = SecondWindow(str(self.fname_one).split("/")[-1].split("'")[0], str(
                    self.fname_two).split("/")[-1].split("'")[0], str(self.combobox.currentText()), str(self.input.text()))
                # self.sw.show()

        except OSError:
            print("Algum erro ocorreu")

    def open_help_window(self):
        try:
            webbrowser.open_new_tab('file://' + os.path.realpath('Help.html'))
        except:
            print("An error ocurred")


# Inicializa a aplicação
def start_app():
    # Aplicação em si
    app = QApplication([])

    app.setStyle('Fusion')

    # Janela Principal
    window = MainWindow()

    # TODO Use layout to make responsive widgets
    # TODO Set alerts for when files have finished downloading
    #window.setMinimumSize(700, 500)
    # Mostrar janela principal
    window.show()

    # Inicializar event loop que persiste o programa
    app.exec()


start_app()
