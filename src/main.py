from fastapi import FastAPI
from route import task_router, user_router
from config.settings import settings
import uvicorn

app = FastAPI(
    title= 'FastAPI Task APP',
    descriptions='this is desc of our app'

)

app.include_router(user_router, tags=['User'],prefix=settings.API_V1_STR)
app.include_router(task_router, tags=['Task'],prefix=settings.API_V1_STR)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=settings.DEBUG_MODE, host=settings.DOMAIN, port=settings.BACKEND_PORT)
