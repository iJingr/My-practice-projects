from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field

class BookCreate(SQLModel):
    title : str = Field(
        max_length=200,
        description='书名'
    )

    author : str = Field(
        max_length=100,
        description='作者'
    )

    price : float = Field(
        gt=0,
        description='价格'
    )

    publish_date : Optional[date] = Field(
        default=None
    )

    description : Optional[str] = Field(
        default=None,
        max_length=1000
    )