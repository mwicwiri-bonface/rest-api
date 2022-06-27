from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    description: str
    published: bool = True
    rating: Optional[int] = None


my_posts = []


def find_post(post_id):
    for post in my_posts:
        if post['id'] == post_id:
            return post


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000)
    my_posts.append(post_dict)
    return {"posts": my_posts}


@app.get("/posts/{post_id}")
async def get_post(post_id: int):
    post = find_post(post_id)
    return {'detail': post}
