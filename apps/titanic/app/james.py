import pandas as pd
from fastapi import FastAPI, Query
from pathlib import Path

from titanic.app.walter import Walter

app = FastAPI(title="Titanic (James)")


class James:
    def __init__(self):
        pass
    
    def get_data_titanic(self):
        w = Walter()
        return w.get_data_titanic()
