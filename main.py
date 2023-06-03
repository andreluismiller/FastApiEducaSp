from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/greet/{name}")
def greet_name(name:str):
    return {"greeting":f"Olá, {name}"}
