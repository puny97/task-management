from pydantic import BaseModel, Field


class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    published_year: int = Field(gt=0)


class BookUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    published_year: int = Field(gt=0)


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
