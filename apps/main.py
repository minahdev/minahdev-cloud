from fastapi import FastAPI, Query

try:
    from titanic.app.james import James
except ModuleNotFoundError:
    from apps.titanic.app.james import James


try:
    from doro.app.doro_diretor import Diretor
except ModuleNotFoundError:
    from apps.doro.app.doro_diretor import Diretor


app = FastAPI(title="Minahdev Cloud Main Page")

@app.get("/")
def read_root():
    return {"message": "FastAPI 메인페이지", "docs": "/docs"}


@app.get("/titanic/data")
def read_titanic_data():
    james = James()
    df = james.get_data_titanic()
    return df.to_dict(orient="records")

@app.get("/doro/data")
def read_doro_data():
    diretor = Diretor()
    df = diretor.get_data_doro()
    return df.to_dict(orient="records")



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)