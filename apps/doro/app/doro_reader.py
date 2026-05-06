import pandas as pd

class Reader:
    def __init__(self):
        pass

    def get_data_doro(self):
        doro_df = pd.read_csv("한국도로공사_교통사고통계_20241231.csv", encoding = "utf-8")
        print(doro_df.head(10))
