import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"

class Walter:
    def __init__(self):
        pass
    
    def get_data_titanic(self):
        df = pd.read_csv(_CSV_PATH)
        # 인덱스 1번 행만 반환 (DataFrame 형태 유지)
        return df.iloc[[0]].astype(object).where(df.iloc[[0]].notna(), None)

    #타이타닉 전체 승객 수
    def titanic_count(self):
        df = pd.read_csv(_CSV_PATH)
        total_passengers = int(df.shape[0])
        return pd.DataFrame([{"total_passengers": total_passengers}])

    #타이타닉 생존자 수
    def titanic_survived(self):
        df = pd.read_csv(_CSV_PATH)
        survived_passengers = int(df["Survived"].fillna(0).astype(int).sum())
        return pd.DataFrame([{"survived_passengers": survived_passengers}])

    #타이타닉 사망자 수
    def titanic_dead(self):
        df = pd.read_csv(_CSV_PATH)
        dead_passengers = int((df["Survived"].fillna(0).astype(int) == 0).sum())
        return pd.DataFrame([{"dead_passengers": dead_passengers}])
