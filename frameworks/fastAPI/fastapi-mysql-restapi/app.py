from fastapi import FastAPI
from routes.user import user

app = FastAPI(
  title="My first FastAPI with MySQL",
  description="Using MySQL locally with Docker",
  version="1.0.0",
  openapi_tags=[{
    "name": "users",
    "description": "users routes",
  }]
)

app.include_router(user)