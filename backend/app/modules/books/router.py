from app.modules.books import service
from app.modules.books.schemas import BookCreate, BookResponse
from fastapi import APIRouter, HTTPException, Query, status

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[BookResponse])
async def get_books(
    search: str | None = Query(
        default=None, description="Search term for filtering books", min_length=1
    ),
):
    return service.get_all_books(search=search)


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int):
    book = service.get_book_by_id(book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return book


@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(book: BookCreate):
    return service.create_book(book.model_dump())


@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book: BookCreate):
    updated_book = service.update_book(book_id, book.model_dump())

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return updated_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    deleted = service.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
