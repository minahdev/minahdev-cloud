from fastapi import FastAPI

from titanic.app.walter_reader import WalterReader
from titanic.app.rose_model import RoseModel
from titanic.app.jack_service import JackService

app = FastAPI(title="Titanic(James)")


class JamesController:
    def __init__(self):
        self.jack = JackService()
    
    #타이타닉 데이터
    def get_data_titanic(self):
        return self.jack.get_data_titanic()
    
    #타이타닉 전체 승객 수
    def titanic_count(self) -> int:
        return self.jack.titanic_count()
    
    #타이타닉 생존자 수
    def titanic_survived(self) -> int:
        return self.jack.titanic_survived()
    
    #타이타닉 사망자 수
    def titanic_dead(self) -> int:
        return self.jack.titanic_dead()

    #결정트리 모델 이름
    def current_model_name(self) -> str:
        return self.jack.current_model_name()

    #결정트리 모델 정확도
    def current_model_accuracy(self) -> float:
        return self.jack.current_model_accuracy()