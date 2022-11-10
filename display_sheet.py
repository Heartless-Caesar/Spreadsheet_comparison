from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QMainWindow, QVBoxLayout, QTableWidgetItem
from PyQt5 import uic
import pandas as pd
import xlwings as xl
import os


class SecondWindow(QWidget):
    def __init__(self, fname_one, fname_two, option):
        super().__init__()
        self.setWindowTitle("Table view")
        self.window_two = QMainWindow()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)
        # self.table = None
        uic.loadUi("table_view.ui")

        try:

            if option == "Sim":
                self.compare_same_shape(fname_one, fname_two)
            else:
                self.compare_sheets(fname_one, fname_two)

        except OSError as e:
            print(f"Error {e}")
            return

    def load_excel_data(self, df_model):

        layout = QVBoxLayout()

        self.setLayout(layout)

        self.table = QTableWidget()

        layout.addWidget(self.table)

        if (df_model.size == 0):
            return

        #df_model.fillna('', inplace=True)

        self.table.setRowCount(len(df_model))
        self.table.setColumnCount(len(df_model.columns))

        self.table.setHorizontalHeaderLabels(df_model.columns)

        for i in range(len(df_model)):
            for j in range(len(df_model.columns)):
                self.table.setItem(i, j, QTableWidgetItem(
                    str(df_model.iloc[i, j])))

    def compare_sheets(self, file_one, file_two):

        # Arquivo 1
        df_1 = pd.read_excel(file_one, index_col=0)

        # Arquivo 2
        df_2 = pd.read_excel(file_two, index_col=0)

        # Merge dos arquivos para comparação
        df_diff = pd.merge(df_1, df_2, how="outer", indicator="Exist")

        # O resultado irá apresentar qual
        df_diff = df_diff.query("Exist != 'both'")

        print(df_diff)

        self.load_excel_data(df_diff)

    def compare_same_shape(self, file_one, file_two):
        # with xl.App(visible=False) as app:
        #     wb_1 = app.books.open(file_one)
        #     ws_1 = wb_1.sheets(1)

        #     wb_2 = app.books.open(file_two)
        #     ws_2 = wb_2.sheets(1)

        #     for cell in ws_2.used_range:
        #         val_ant = ws_1.range((cell.row, cell.column)).value
        #         if cell.value != val_ant:
        #             cell.api.AddComment(f"Valor de {wb_1.name}: {val_ant}")
        #             cell.color = (255, 71, 76)

        df_1 = pd.read_excel(file_one, index_col=0)

        df_2 = pd.read_excel(file_two, index_col=0)

        if df_1.shape == df_2.shape:

            df_diff = df_1.compare(df_2)

            print(df_diff)

            df_diff.to_excel(os.getcwd() + "/Diff.xlsx")

        else:
            print("Files are not similar")
