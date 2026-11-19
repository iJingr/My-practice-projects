from typing import List, Optional, Dict
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from orm.database import get_session
from orm.models import Book
from orm.schemas import BookCreate
import services.book_crud as CRUD

book_router = APIRouter(prefix='/books', tags=['图书管理'])

@book_router.post('/', response_model=Book, status_code=201)
async def create_book(data: BookCreate, session: AsyncSession = Depends(get_session)):
    return await CRUD.create_book(session, data)

async def pagination_params(
        skip: int = Query(default=0, ge=0, description='跳过N条'),
        limit: int = Query(default=10, ge=1, le=100, description='每页条数')
) -> Dict:
    return {'skip' : skip, 'limit' : limit}

@book_router.get('/', response_model=List[Book])
async def get_book_list(
        session: AsyncSession = Depends(get_session),
        title: Optional[str] = Query(default=None, description='书名关键词'),
        page: Dict = Depends(pagination_params)
):
    return await CRUD.get_books(
        session,
        title_keyword=title,
        skip=page['skip'],
        limit=page['limit']
    )

@book_router.get('/{book_id}', response_model=Book)
async def get_book_by_id(
        book_id: int,
        session: AsyncSession = Depends(get_session)
):
    book = await CRUD.get_book_by_id(session, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f'图书 id:{book_id} 不存在')

    return book

@book_router.put('/{book_id}', response_model=Book)
async def update_book(
        book_id: int,
        data: BookCreate,
        session: AsyncSession = Depends(get_session)
):
    book = await CRUD.update_book(book_id=book_id, data=data, session=session)
    if not book:
        raise HTTPException(status_code=404, detail=f'图书 id:{book_id} 不存在')

    return book

@book_router.delete('/{book_id}')
async def book_delete(
        book_id: int,
        session: AsyncSession = Depends(get_session)
):
    deleted = await CRUD.delete_book(book_id=book_id, session=session)
    if not deleted:
        raise HTTPException(status_code=404, detail=f'图书 id:{book_id} 不存在')
    return {'message' : f'图书 id:{book_id} 已删除'}

