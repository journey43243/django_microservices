from fastapi import Fastapi
import uvicorn

app = Fastapi()


@app.get('home')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    uvicorn.run('main:app', port = 8000)