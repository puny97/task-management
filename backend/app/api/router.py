from fastapi import APIRouter

from app.modules.books.router import router as books_router

router = APIRouter()

router.include_router(books_router)


@router.get("/")
def root():
    return {"message": "Welcome to FASTAPI!"}
