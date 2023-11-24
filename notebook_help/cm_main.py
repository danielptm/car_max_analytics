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



def suv_mean_price(df: pd.DataFrame):
    filtered = df[df['vehicle_type'].str.contains("SUV")]
    suv_mean = filtered.loc[:, "price"].mean()
    return suv_mean


def non_suv_mean_price(df: pd.DataFrame):
    filtered = df[~df['vehicle_type'].str.contains("SUV")]
    non_suv_mean = filtered.loc[:, "price"].mean()
    return non_suv_mean

def add_precentile_price_column(df: pd.DataFrame):
    df['percentile_price'] = pd.qcut(df['price'], 10, labels=False)
    return df

def add_precentile_appraisal_offer_column(df: pd.DataFrame):
    df['percentile_appraisal_offer'] = pd.qcut(df['appraisal_offer'], 10, labels=False)
    return df



