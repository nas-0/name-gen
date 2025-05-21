from fastapi import FastAPI

app = FastAPI()


def return_name(name):
    return {"first_name": name}

@app.get("/names")
def homepage():
    name = return_name("sheraz")
    return name

