import pandas as pd

def show_data(data_path: str):
     df = pd.read_csv(data_path)
     return df
