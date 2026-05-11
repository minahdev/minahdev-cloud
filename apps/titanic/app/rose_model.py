from sklearn.tree import DecisionTreeClassifier

class RoseModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def model_name(self) -> str:
        return type(self.model).__name__