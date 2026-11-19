from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date

# 建立数据库表每一行有哪些字段
class Book(SQLModel, table=True):
    id : Optional[int] = Field(
        default=None,
        primary_key=True
    )

    title : str = Field(
        index=True,
        nullable=False,
        max_length=200
    )

    author : str = Field(
        nullable=False,
        max_length=100
    )

    publish_date : Optional[date] = Field(
        default=None
    )

    price : float = Field(
        gt=0
    )

    description : Optional[str] = Field(
        default=None,
        max_length=1000
    )