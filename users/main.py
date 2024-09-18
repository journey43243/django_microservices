from fastapi import FastAPI
import uvicorn
import time
from requests import request
from data_models import UserRequiredParametrs
from database.orm import create_tables, drop_tables,create_user
app = FastAPI()

@app.get('/get_token')
def main():
    drop_tables()
    create_tables()
    return 'done'


def gen_jwt():
    pass

@app.post('/users/registration')
async def registration(user : UserRequiredParametrs):
    await create_user(username= user.username,
                      password=user.password,
                      email= user.email)
    return {
        'status code' : 201,
        'user' : user.username
    }
# if __name__ == "__main__":
#     uvicorn.run("main:app", port = 8000,reload = True)