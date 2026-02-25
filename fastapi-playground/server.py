from fastapi import FastAPI
app=FastAPI()

       
@app.get("/")
def greet():
    return "Greetings from fastapi ,i'm a python web framework"