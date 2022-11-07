from PyQt5.QtWidgets import QWidget,QTableWidget, QTableWidgetItem, QHeaderView, QApplication, QMainWindow, QVBoxLayout, QPushButton
from PyQt5 import uic
import pandas as pd

class display_sheet(QWidget):
    def __init__(self):
        super(display_sheet,self).__init__()
        
        self.window = QMainWindow()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)
        uic.loadUi("table_view.ui")
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.button = QPushButton("Button")
        layout.addWidget(self.button)

    def load_excel_data(self, df_model):

        if(df_model.size == 0):
            return 

        df_model.fillna('',inplace=True)
        self.table.setRowCount(df_model.shape[0])
        self.table.setRowCount(df_model.shape[1])
        self.table.setHorizontalHeaderLabels(df_model.columns)       
        
        self.table.setModel(df_model)

    def pass_data(self,data):
        self.load_excel_data(self,data)
    
    def compare_sheets(file_one, file_two):  
        
        # Arquivo 1
        df_1 = pd.read_excel(file_one, index_col=0)
        
        # Arquivo 2
        df_2 = pd.read_excel(file_two, index_col=0)

        # Merge dos arquivos para comparação
        df_diff = pd.merge(df_1,df_2,how="outer",indicator="Exist")

        # O resultado irá apresentar qual 
        df_diff = df_diff.query("Exist != 'right_only'")

        display_sheet.load_excel_data(df_diff)

        print(df_diff)    