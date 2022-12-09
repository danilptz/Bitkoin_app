import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

response = {"Ответ": "Который возвращает сервер"}


@api.get('/static/path')
def hello():
    return "hello"


@api.get('/user/{nick}')
def get_nick(nick):
    return {"user": nick}


@api.get('/userid/{id : int}')
def get_id():
    return {"user": "id"}


@api.get('/user_id/{id}')
def get_id2(id: int):
    return {"user": id}


@api.get('/user_id_str/{id}')
def get_id2(id):
    return {"user": id}


@api.get('/test/{id:int}/{text:str}/{custom_path:path}')
def get_test(id, text, custom_path):
    return {"id": id,
            "": text,
            "custom_path": custom_path}


fake_database = {'users': [
    {
        "id": 1,
        "name": "Anna",
        "nick": "Anny42",
        "balance": 15300
    },
    {
        "id": 2,
        "name": "Dima",
        "nick": "dimon2319",
        "balance": 160.23
    },
    {
        "id": 3,
        "name": "Vladimir",
        "nick": "vova777",
        "balance": "25000"
    }
], }


@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id - 1]


@api.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id - 1]['balance']


@api.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance
