from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):  # O parâmetro da  função traz o objeto (schema de lá)

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()  # converte o objeto do pydantic em um dicionário
    )

    database.append(user_with_id)

    return user_with_id

@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}

@app.get('/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def read_users_id(user_id: int):
    if user_id < 1 or user_id > len(database) + 1:

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return database[user_id - 1]

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    
    if user_id < 1 or user_id > len(database) + 1:

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
                            
    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database) + 1:

        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
        
    del database[user_id - 1]
    
    return {'Message' : 'User deleted'}
