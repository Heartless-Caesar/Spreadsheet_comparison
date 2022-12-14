from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5 import uic
import pandas as pd


class SecondWindow(QWidget):
    def __init__(self, fname_one, fname_two, option, inputData):
        super().__init__()
        self.setWindowTitle("Table view")
        self.dialog = QFileDialog()
        self.input = inputData
        self.window_two = QMainWindow()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)

        uic.loadUi("table_view.ui")

        try:

            if option == "Sim":
                self.compare_same_shape(fname_one, fname_two)
            else:
                self.compare_different_shape(fname_one, fname_two)

        except OSError as e:
            print(f"Error {e}")
            return

    def compare_different_shape(self, file_one, file_two):

        # Arquivo 1
        df_1 = pd.read_excel(file_one, index_col=0)

        # Arquivo 2
        df_2 = pd.read_excel(file_two, index_col=0)

        # Merge dos arquivos para comparação
        df_diff = pd.merge(df_1, df_2, how="outer", indicator="Exist").rename(
            {'left_only': '1', 'right_only': '2'})

        # O resultado irá apresentar qual
        df_diff = df_diff.query("Exist != 'both'")

        folder_path = self.dialog.getExistingDirectory(None, "Select folder")

        df_diff.to_excel(f"{folder_path}/{self.input}.xlsx")

    def compare_same_shape(self, file_one, file_two):
        df_1 = pd.read_excel(file_one, index_col=0)

        df_2 = pd.read_excel(file_two, index_col=0)

        if df_1.shape == df_2.shape:

            df_diff = df_1.reset_index(drop=True).compare(
                df_2.reset_index(drop=True)).rename(
                columns={'self': '1', 'other': '2'})

            # print(df_diff)

            folder_path = self.dialog.getExistingDirectory(
                None, "Select folder")

            df_diff.to_excel(f"{folder_path}/{self.input}.xlsx")

            # pd.read_excel(f"~/Documents/{self.input}.xlsx")

        else:
            print("Files are not similar")

    # def load_excel_data(self, df_model):

    #     layout = QVBoxLayout()

    #     self.setLayout(layout)

    #     self.table = QTableWidget()

    #     layout.addWidget(self.table)

    #     if (df_model.size == 0):
    #         return

    #     df_model.fillna('', inplace=True)

    #     self.table.setRowCount(len(df_model))
    #     self.table.setColumnCount(len(df_model.columns))

    #     self.table.setHorizontalHeaderLabels(df_model.columns)

    #     for i in range(len(df_model)):
    #         for j in range(len(df_model.columns)):
    #             self.table.setItem(i, j, QTableWidgetItem(
    #                 str(df_model.iloc[i, j])))
