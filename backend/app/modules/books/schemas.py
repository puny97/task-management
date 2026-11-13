from typing import Any

from app.modules.books.utils import validate_year
from pydantic import BaseModel, Field, field_validator


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    published_year: int

    @field_validator("title", "author", mode="before")
    @classmethod
    def validate_text_fields(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()

        if not value:
            raise ValueError("Field cannot be empty or whitespace")
        return value

    @field_validator("published_year")
    @classmethod
    def validate_published_year(cls, value: int) -> int:
        return validate_year(value)


class BookUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    published_year: int

    @field_validator("title", "author", mode="before")
    @classmethod
    def validate_text_fields(cls, value: Any) -> Any:
        if isinstance(value, str):
            value = value.strip()

            if not value:
                raise ValueError("Field cannot be empty or whitespace")

        return value

    @field_validator("published_year")
    @classmethod
    def validate_published_year(cls, value: int) -> int:
        return validate_year(value)


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    published_year: int


class BookListResponse(BaseModel):
    items: list[BookResponse]
    total: int
    page: int
    limit: int
    total_pages: int
