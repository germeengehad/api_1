from fastapi import FastAPI , Body
from fastapi import APIRouter
from schema import  Task , Score 

task_router = APIRouter(
    prefix="/task", 
    tags=["Task"]
    )

@task_router.post('/task')
def add_task(task: Task = Body(...)):
    return {'msg': 'Task added successfully', **task.dict()}

@task_router.get('/task/{id}')
def get_task(id: int, name: str):
    return f'Task: Id is {id} and name is {name} retrieved successfully'

@task_router.put('/task/{id}')
def update_task(id: int, name: str, score: Score = Body(...)):
    return {'msg': f'Task: ID is {id} and name is {name} updated successfully', **score.dict()}

@task_router.delete('/task/{id}')
def delete_task(id: int, name: str):
    return f'Task: ID is {id} and name is {name} deleted successfully'