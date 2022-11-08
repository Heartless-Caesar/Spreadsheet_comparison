from PyQt5.QtWidgets import QWidget,QTableWidget, QTableWidgetItem, QHeaderView, QApplication, QMainWindow, QVBoxLayout, QPushButton,QTableWidgetItem
from PyQt5.QtCore import QAbstractTableModel
from PyQt5 import uic
import pandas as pd

class SecondWindow(QWidget):
    def __init__(self,fname_one,fname_two,parent=None):
        super().__init__()
        self.setWindowTitle("Table view")
        self.window_two = QMainWindow()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)
        #self.table = None
        uic.loadUi("table_view.ui")

        try:
            self.compare_sheets(fname_one,fname_two)
        except:
            print("An error occured")    
    
    def load_excel_data(self, df_model):

        layout = QVBoxLayout()
        
        self.setLayout(layout)
        
        self.table = QTableWidget()
        
        layout.addWidget(self.table)

        if(df_model.size == 0):
            return 

        # df_model.fillna('',inplace=True)

        self.table.setRowCount(len(df_model))
        self.table.setColumnCount(len(df_model.columns))

        self.table.setHorizontalHeaderLabels(df_model.columns)

        for i in range(len(df_model)):
            for j in range(len(df_model.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(df_model.iloc[i,j])))

    
    def compare_sheets(self, file_one, file_two):  
        
        # Arquivo 1
        df_1 = pd.read_excel(file_one, index_col=0)
        
        # Arquivo 2
        df_2 = pd.read_excel(file_two, index_col=0)

        # Merge dos arquivos para comparação
        df_diff = pd.merge(df_1,df_2,how="outer",indicator="Exist")

        # O resultado irá apresentar qual 
        df_diff = df_diff.query("Exist != 'both'")

        self.model = df_diff
        self._data = df_diff

        self.load_excel_data(df_diff)

    