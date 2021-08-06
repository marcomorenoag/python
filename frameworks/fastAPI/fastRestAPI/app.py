from fastapi import FastAPI, HTTPException
from typing import Text
from pydantic import BaseModel
from typing import Text, Optional
from datetime import datetime
from uuid import uuid4 as uuid


app = FastAPI()

posts = []

# Post Model
class Post(BaseModel):
  id: Optional[str]
  title: str
  author: str
  content: Text
  created_at: datetime = datetime.now()
  published_at: Optional[datetime]
  published: bool = False


@app.get('/')
def read_root():
  return { 'welcome': 'Welcome to my REST API' }

@app.get('/posts')
def get_posts():
  return posts

@app.post('/posts')
def save_post(post: Post):
  post.id = str(uuid())
  posts.append(post.dict())
  return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id: str):
  for post in posts:
    if post['id'] == post_id:
      return post
  raise HTTPException(status_code=404, detail='Post Not Found')

@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
  for idx, post in enumerate(posts):
    if post['id'] == post_id:
      posts.pop(idx)
      return { 'message': 'Post deleted successfully!' }
  raise HTTPException(status_code=404, detail='Post Not Found')

@app.put('/posts/{post_id}')
def update_post(post_id: str, updated_post: Post):
  for idx, post in enumerate(posts):
    if post['id'] == post_id:
      posts[idx]['title'] = updated_post.title
      posts[idx]['content'] = updated_post.content
      posts[idx]['author'] = updated_post.author
      return { 'message': 'Post has been updated successfully!' }
  return HTTPException(status_code=404, detail='Post Not Found')