from fastapi import FastAPI, Query

from titanic.app.james import James

from doro.app.doro_diretor import Diretor


app = FastAPI(title="Minahdev Cloud Main Page")

@app.get("/")
def read_root():
    return {"message": "FastAPI 메인페이지", "docs": "/docs"}

#타이타닉 데이터
@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data_titanic()
    return df.to_dict(orient="records")


#타이타닉 전체 승객 수
@app.get("/titanic/count")
def read_titanic_count():
    james = James()
    df = james.titanic_count()
    return df.to_dict(orient="records")


#타이타닉 생존자 수
@app.get("/titanic/count/survived")
def read_titanic_survived():
    james = James()
    df = james.titanic_survived()
    return df.to_dict(orient="records")


#타이타닉 사망자 수
@app.get("/titanic/count/dead")
def read_titanic_dead():
    james = James()
    df = james.titanic_dead()
    return df.to_dict(orient="records")



#타이타닉 결정트리 모델 파일 존재 여부
@app.get("/titanic/tree")
def read_titanic_tree():
    james = James()
    has_model = james.has_decision_tree_model()
    return {"has_model": has_model}



@app.get("/doro/data")
def read_doro_data():
    diretor = Diretor()
    df = diretor.get_data_doro()
    return df.to_dict(orient="records")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)