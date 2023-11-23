import pandas as pd


def show_data(data_path: str):
    df = pd.read_csv(data_path)
    return df


def count_car_makes(df: pd.DataFrame):
    res = df.groupby("make_appraisal").size()
    return res


def count_car_models(df: pd.DataFrame):
    res = df.groupby("model_appraisal").size()
    return res
