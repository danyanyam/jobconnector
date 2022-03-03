# по get-запросам должен возвращать резюме людей.
from database import resumes
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def get_root():
    pass


@app.get('/resume')
def get_resume():
    return resumes[0]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")
