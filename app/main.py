from random import randrange
from typing import Optional
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from starlette import status

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


@app.post("/posts",  status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000)
    my_posts.append(post_dict)
    return {"posts": my_posts}


@app.get("/posts/{post_id}",  status_code=status.HTTP_200_OK)
async def get_post(post_id: int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return {'detail': post}


def find_post_index(post_id):
    for index, post in enumerate(my_posts):
        if post['id'] == post_id:
            return index


@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    index = find_post_index(post_id)
    if index:
        my_posts.pop(index)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)