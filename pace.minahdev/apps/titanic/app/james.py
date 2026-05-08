from fastapi import FastAPI

from titanic.app.walter import Walter
from titanic.app.rose import Rose

app = FastAPI(title="Titanic(James)")


class James:
    def __init__(self):
        pass
    
    #타이타닉 데이터
    def get_data_titanic(self):
        w = Walter()
        return w.get_data_titanic()
    
    #타이타닉 전체 승객 수
    def titanic_count(self):
        w = Walter()
        return w.titanic_count()
    
    #타이타닉 생존자 수
    def titanic_survived(self):
        w = Walter()
        return w.titanic_survived()
    
    #타이타닉 사망자 수
    def titanic_dead(self):
        w = Walter()
        return w.titanic_dead()

    #결정트리 모델 파일 존재 여부
    def has_decision_tree_model(self) -> bool:
        r = Rose()
        return r.model_path.exists()

