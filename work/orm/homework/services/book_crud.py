from datetime import date
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from orm.models import Book
from orm.schemas import BookCreate

# Create
async def create_book(session: AsyncSession, data: BookCreate) -> Book:
    book = Book(**data.model_dump())

    session.add(book)
    await session.commit()
    await session.refresh(book)
    return book

# Research
async def get_books(
        session: AsyncSession,
        title_keyword: Optional[str] = None,
        skip: int = 0,
        limit: int = 10
) -> List[Book]:
    statement = select(Book)
    if title_keyword:
        statement = statement.where(Book.title.contains(title_keyword))
    statement = statement.offset(skip).limit(limit)
    result = await session.execute(statement)
    return result.scalars().all()

async def get_book_by_id(session: AsyncSession, book_id: int) -> Optional[Book]:
    return await session.get(Book, book_id)

async def update_book(session: AsyncSession, book_id: int, data: BookCreate) -> Optional[Book]:
    book = await session.get(Book, book_id)
    if not book:
        return None
    book.title = data.title
    book.author = data.author
    book.price = data.price
    if data.publish_date is not None:
        book.publish_date = data.publish_date
    if data.description is not None:
        book.description = data.description
    await session.commit()
    await session.refresh(book)
    return book

async def delete_book(session: AsyncSession, book_id: int) -> bool:
    book = await session.get(Book, book_id)
    if not book:
        return False
    await session.delete(book)
    await session.commit()
    return True
