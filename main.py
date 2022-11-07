from PyQt5.QtWidgets import QApplication, QPushButton,QLabel, QFileDialog,QDialog,QComboBox,QMainWindow, QMessageBox
from display_sheet import display_sheet
from PyQt5 import uic

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Carrega o arquivo UI que será utilizado
        self.window = uic.loadUi("sheets.ui",self)
        
        # CArrega tela para alertas diversos
        self.message = QMessageBox()

        # Propriedades que irão ter o nome do arquivo para o pandas processar
        self.fname_one = ""
        self.fname_two = ""

        # Selecionar se os arquivos tem o mesmo numero de 
        self.combobox = self.findChild(QComboBox,"comboBox")
        self.combobox.addItems(["Sim","Não"])

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
        self.execute_button.clicked.connect(self.open_second_window)
        self.execute_button.clicked.connect(lambda _, xl_path="test",sheet_name="tes":display_sheet.load_excel_data(xl_path,sheet_name))

    def open_file_dialog_one(self):
         self.fname_one = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;(*.ods);;All Files (*)")   

         if self.fname_one:
            self.label_one.setText(str(self.fname_one).split("/")[-1].split("'")[0])

    def open_file_dialog_two(self):
         self.fname_two = QFileDialog.getOpenFileName(self, "Selecione um arquivo","","(*.xlsx);;(*.ods);;All Files (*)")   

         if self.fname_two:
            self.label_two.setText(str(self.fname_two).split("/")[-1].split("'")[0])  

    def executar_processamento(self):
        if (self.fname_one or self.fname_two != ""): 
            display_sheet.compare_sheets(str(self.fname_one).split("/")[-1].split("'")[0],str(self.fname_two).split("/")[-1].split("'")[0])   
        self.message.setText("One of the directories is empty")
        #self.message.show()
        return        

    def open_second_window(self):
       self.ui = display_sheet(self)
       self.ui.show()


# Inicializa a aplicação
def start_app():
    # Aplicação em si
    app = QApplication([])

    app.setStyle('Fusion')
    
    # Janela Principal
    window = MainWindow()

    # Mostrar janela principal
    window.show()

    # Inicializar event loop que persiste o programa
    app.exec()



start_app()
    