from fastapi import FastAPI , Body
from fastapi import APIRouter
from schema import User, Product

user_router = APIRouter(
    prefix="/user", 
    tags=["User"]
    )


@user_router.post('/user')
def add_user(user: User = Body(...)):
    return {'msg': 'User added successfully', **user.dict()}

@user_router.get('/user/{id}')
def get_user(id: int, name: str):
    return f'User: Id is {id} and name is {name} retrieved successfully'

@user_router.put('/user/{id}')
def update_user(id: int, name: str, product: Product = Body(...)):
    return {'msg': f'User: ID is {id} and name is {name} updated successfully', **product.dict()}

@user_router.delete('/user/{id}')
def delete_user(id: int, name: str):
    return f'User: ID is {id} and name is {name} deleted successfully'