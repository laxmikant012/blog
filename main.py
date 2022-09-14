from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'laxmikant'}}

@app.get('/about')
def about():
    return {"data":{"bunty":"pussy"}}