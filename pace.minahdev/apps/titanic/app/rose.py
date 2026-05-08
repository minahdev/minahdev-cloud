from __future__ import annotations

from pathlib import Path

import pandas as pd

try:
    from joblib import dump, load
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.tree import DecisionTreeClassifier
except Exception as e:  # pragma: no cover
    _SKLEARN_IMPORT_ERROR = e
else:
    _SKLEARN_IMPORT_ERROR = None


_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.joblib"


class Rose:
    def __init__(self, model_path: Path | None = None):
        self.model_path = model_path or _MODEL_PATH

    def save_decision_tree_model(self) -> dict:
        """
        Train a Titanic survival Decision Tree pipeline and save it to disk.
        Returns basic metadata so callers can show the result.
        """
        if _SKLEARN_IMPORT_ERROR is not None:
            raise ImportError(
                "scikit-learn/joblib is required to train & save the model. "
                "Install dependencies (e.g. `pip install scikit-learn joblib`)."
            ) from _SKLEARN_IMPORT_ERROR

        df = pd.read_csv(_CSV_PATH)
        if "Survived" not in df.columns:
            raise ValueError("CSV must contain 'Survived' column.")

        y = df["Survived"].astype(int)
        X = df[
            [
                "Pclass",
                "Sex",
                "Age",
                "SibSp",
                "Parch",
                "Fare",
                "Embarked",
            ]
        ].copy()

        numeric_features = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
        categorical_features = ["Sex", "Embarked"]

        numeric_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
            ]
        )
        categorical_transformer = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="most_frequent")),
                ("onehot", OneHotEncoder(handle_unknown="ignore")),
            ]
        )

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

        model = DecisionTreeClassifier(
            random_state=42,
            max_depth=5,
        )

        clf = Pipeline(
            steps=[
                ("preprocess", preprocessor),
                ("model", model),
            ]
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        clf.fit(X_train, y_train)
        score = float(clf.score(X_test, y_test))

        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        dump(clf, self.model_path)

        return {
            "model_path": str(self.model_path),
            "test_accuracy": score,
            "rows": int(df.shape[0]),
            "features": list(X.columns),
        }

    def load_model(self):
        if _SKLEARN_IMPORT_ERROR is not None:
            raise ImportError(
                "scikit-learn/joblib is required to load the model."
            ) from _SKLEARN_IMPORT_ERROR
        return load(self.model_path)