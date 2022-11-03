from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel, QLineEdit, QVBoxLayout,QWidget,QInputDialog,QFileDialog,QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from select_file import App
import sys
import os

# otherDirectory = os.chdir("")

# currentDirectory = os.getcwd()

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Carrega o arquivo UI que será utilizado
        uic.loadUi("sheets.ui",self)

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

    def open_file_dialog_one(self):
         fname = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;All Files (*)")   

         if fname:
            self.label_one.setText(str(fname).split("/")[-1].split("'")[0])

    def open_file_dialog_two(self):
         fname = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;All Files (*)")   

         if fname:
            self.label_two.setText(str(fname).split("/")[-1].split("'")[0])        


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
    