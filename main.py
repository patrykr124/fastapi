from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {'data': {'name': "Patryk"}}

@app.get("/about")
def index():
    return {'data': {'name': "About page!"} }