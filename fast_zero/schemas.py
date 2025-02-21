from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age: int
    password: str


class UserDB(UserSchema):  
    id: int


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int


class UserList(BaseModel):
    users: list = [UserPublic]  
