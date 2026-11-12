from app.modules.books.data import books


def get_all_books():
    return books


def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    return None


def create_book(book_data: dict):
    new_id = max((book["id"] for book in books), default=0) + 1

    new_book = {"id": new_id, **book_data}

    books.append(new_book)

    return new_book


def update_book(book_id: int, book_data: dict):

    book = get_book_by_id(book_id)

    if book is None:
        return None

    book.update(book_data)
    return book


def delete_book(book_id: int):

    book = get_book_by_id(book_id)

    if book is None:
        return False

    books.remove(book)
    return True
