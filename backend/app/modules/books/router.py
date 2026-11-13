from typing import Annotated, Literal

from app.modules.books import service
from app.modules.books.schemas import BookCreate, BookListResponse, BookResponse
from fastapi import APIRouter, HTTPException, Query, status
from pydantic import AfterValidator

router = APIRouter(prefix="/books", tags=["Books"])


def validate_year(year: int) -> int:
    if year == 0:
        raise ValueError("Published year cannot be 0")

    return year


@router.get("/", response_model=BookListResponse)
def get_books(
    search: str | None = Query(
        default=None, description="Search term for filtering books", min_length=1
    ),
    author: str | None = Query(
        default=None, description="Filter books by author", min_length=1
    ),
    published_year: Annotated[
        int | None, Query(), AfterValidator(validate_year)
    ] = None,
    sort_by: Literal["id", "title", "author", "published_year"] = "id",
    order: Literal["asc", "desc"] = "asc",
    page: int = Query(default=1, description="Page number for pagination", gt=0),
    limit: int = Query(
        default=10, description="Number of items per page", gt=0, le=100
    ),
):
    return service.get_all_books(
        search=search,
        author=author,
        published_year=published_year,
        sort_by=sort_by,
        order=order,
        page=page,
        limit=limit,
    )


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = service.get_book_by_id(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    return service.create_book(book.model_dump())


@router.put("/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate):
    updated_book = service.update_book(book_id, book.model_dump())

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return updated_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    deleted = service.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
