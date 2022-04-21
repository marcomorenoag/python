from fastapi import FastAPI

app = FastAPI()

students = {
  1: {
    "name": "John",
    "age": 17,
    "class": "Year 12"
  },
}

@app.get("/")
def index():
  return { "name": "First Data" }

@app.get("/student/{id}")
def get_student(id: int):
  return students[id]