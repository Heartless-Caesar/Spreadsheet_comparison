from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel, QLineEdit, QVBoxLayout,QWidget,QInputDialog,QFileDialog,QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from compare_sheets import ProcessarDados
import sys
import os

# otherDirectory = os.chdir("")

# currentDirectory = os.getcwd()

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Carrega o arquivo UI que será utilizado
        uic.loadUi("sheets.ui",self)
        
        # Propriedades que irão ter o nome do arquivo para o pandas processar
        self.fname_one = ""
        self.fname_two = ""

        # Elementos do UI que serão manipulados de alguma forma
        self.select_file_one_button = self.findChild(QPushButton,"select_file_one_button")
        self.select_file_two_button = self.findChild(QPushButton,"select_file_two_button")
        self.execute_button = self.findChild(QPushButton,"execute_button")
        self.cancel_button = self.findChild(QPushButton,"cancel_button")

        # Label arquivo 1
        self.label_one = self.findChild(QLabel,"label")
        
        # Label arquivo 2  
        self.label_two = self.findChild(QLabel,"label_2")

        # Opens dialog
        self.select_file_one_button.clicked.connect(self.open_file_dialog_one)
        self.select_file_two_button.clicked.connect(self.open_file_dialog_two)

        # Executa comparacao de planilhas
        self.execute_button.clicked.connect(self.executar_processamento)

    def open_file_dialog_one(self):
         self.fname_one = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;All Files (*)")   

         if self.fname_one:
            self.label_one.setText(str(self.fname_one).split("/")[-1].split("'")[0])

    def open_file_dialog_two(self):
         self.fname_two = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;All Files (*)")   

         if self.fname_two:
            self.label_two.setText(str(self.fname_two).split("/")[-1].split("'")[0])  

    def executar_processamento(self):
        ProcessarDados.compare_sheets(self.fname_one,self.fname_two)              


# Inicializa a aplicação
def start_app():
    # Aplicação em si
    app = QApplication([])

    # Janela Principal
    window = MainWindow()

    # Mostrar janela principal
    window.show()

    # Inicializar event loop que persiste o programa
    app.exec()



start_app()
    