from typing import Union

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: Union[str, None] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    posts: list[Post] = []

    class Config:
        orm_mode = True
