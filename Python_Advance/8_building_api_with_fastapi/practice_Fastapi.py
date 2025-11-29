#import FastAPI
from fastapi import FastAPI

#Create an object using FastAPI
app = FastAPI()

#define an endpoint to return hello
@app.get("/")
def hello():
    return "Hello"

#define second endpoint to return hello name

@app.get("/hello/{name}")
def hello(name):
    return f"Hello {name}!"




""" in the terminal write fastapi dev .\practice_fastapi.py"""