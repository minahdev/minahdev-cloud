import pandas as pd
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "한국도로공사_교통사고통계_20241231.csv"

class Reader:
    def __init__(self):
        pass

    def get_data_doro(self):
        df = pd.read_csv(_CSV_PATH, encoding="euc-kr")
        # 인덱스 1번 행만 반환 (DataFrame 형태 유지)
        return df.iloc[[1]].astype(object).where(df.iloc[[1]].notna(), None)


    # def head_records(self, n: int = 10) -> list[dict]:
    #    df = self.get_data_doro().head(n)
    #    pandas의 NaN은 JSON 직렬화에서 에러가 나므로 None으로 변환
    #    df = df.astype(object).where(pd.notna(df),None)
    #    return df.to_dict(orient="records")
    

