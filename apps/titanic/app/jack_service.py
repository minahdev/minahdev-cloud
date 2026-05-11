from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"


class JackService:
    def __init__(self):
        self.walter = WalterReader()
        self.rose = RoseModel()
    
    #타이타닉 데이터
    def get_data_titanic(self):
        return self.walter.get_data_titanic()
    
    #타이타닉 전체 승객 수
    def titanic_count(self) -> int:
        return self.walter.titanic_count()
    
    #타이타닉 생존자 수
    def titanic_survived(self) -> int:
        return self.walter.titanic_survived()
    
    #타이타닉 사망자 수
    def titanic_dead(self) -> int:
        return self.walter.titanic_dead()
        

    #결정트리 모델 이름
    def current_model_name(self) -> str:
        return self.rose.model_name()

    #결정트리 모델 정확도
    def current_model_accuracy(self) -> float:
        df = pd.read_csv(_CSV_PATH)
        df = df.dropna(subset=["Survived"])

        X = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]].copy()
        X["Sex"] = X["Sex"].map({"male": 0, "female": 1})
        X = X.fillna(X.median(numeric_only=True))
        y = df["Survived"].astype(int)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        model = self.rose.model
        model.fit(X_train, y_train)
        return float(model.score(X_test, y_test))