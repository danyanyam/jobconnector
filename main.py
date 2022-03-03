from typing import Dict as D
from resume import ResumeHandler
from fastapi import FastAPI
import uvicorn


app = FastAPI()
rh = ResumeHandler()


@app.get('/')
def get_root():
    pass


@app.post('/resume/filter')
def post_filter(filters: D[str, str]):
    return rh.filter(filters)


@app.get('/filters')
def get_filters():
    return rh.get_filters()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")
