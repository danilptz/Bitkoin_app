import fastapi
from fastapi import  Request


api = fastapi.FastAPI()


@api.get('/')
@api.post('/')
@api.put('/')
@api.delete('/')
def index(request: Request):
    return {"Reqwest":[request.method,
                       request.headers]}
