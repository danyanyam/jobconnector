from typing import Dict as D, List as L, Union

import fastapi


from resume import ResumeHandler
from fastapi import FastAPI
from parameters import examples
import uvicorn


app = FastAPI()
rh = ResumeHandler()


@app.post('/resume/filter')
def post_filter(filter: fastapi.Body(..., example=examples['filter'])) -> L[D[str, str]]:
    """
    Filters resumes by given dictionary as follows:

    Let filter be {"experience": "2 years"},
    function iterates over all resumes and looks for
    specific ones with every condition met
    """
    return rh.filter(filter)


@app.get('/filters')
def get_filters():
    return rh.get_filters()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001, log_level="info")
