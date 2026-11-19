from contextlib import asynccontextmanager
from fastapi import FastAPI

from orm.database import init_db
from routers.books import book_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan, title='图书管理系统2.0')

app.include_router(book_router)

@app.get('/')
async def root():
    return {'message':'图书管理系统2.0已启动'}