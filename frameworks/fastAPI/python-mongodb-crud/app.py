from fastapi import FastAPI
from docs import tags_metadata
# Routes
from routes.user import user


app = FastAPI(
  title="REST API with FastAPI and Mongodb",
  description="This is a simple REST API using fastapi and mongodb",
  version="0.0.1",
  openapi_tags=tags_metadata
)

app.include_router(user)