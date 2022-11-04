# from pandas import DataFrame,read_excel
import pandas as pd

class ProcessarDados():
    def __init__(self):
        super(ProcessarDados,self).__init__()


    def compare_sheets(file_one, file_two):  
        
        # Arquivo 1
        df_1 = pd.read_excel(file_one, index_col=0)
        
        # Arquivo 2
        df_2 = pd.read_excel(file_two, index_col=0)

        # Merge dos arquivos para comparação
        df_diff = pd.merge(df_1,df_2,how="outer",indicator="Exist")

        # O resultado irá apresentar qual 
        df_diff = df_diff.query("Exist != 'right_only'")

        print(df_diff)
