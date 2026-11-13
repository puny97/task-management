from app.modules.books.data import books


def get_all_books(
    search=None,
    author=None,
    published_year=None,
    sort_by="id",
    order="asc",
    page=1,
    limit=10,
):

    filtered_books = books.copy()

    if search:
        search_lower = search.strip().lower()

        filtered_books = [
            book
            for book in filtered_books
            if search_lower in book["title"].lower()
            or search_lower in book["author"].lower()
        ]

    if author:
        author_lower = author.strip().lower()

        filtered_books = [
            book for book in filtered_books if author_lower in book["author"].lower()
        ]

    if published_year:
        filtered_books = [
            book for book in filtered_books if book["published_year"] == published_year
        ]

    total = len(filtered_books)

    filtered_books.sort(
        key=lambda book: (
            book[sort_by].lower() if isinstance(book[sort_by], str) else book[sort_by]
        ),
        reverse=order == "desc",
    )

    start = (page - 1) * limit
    end = start + limit

    paginated_books = filtered_books[start:end]

    total_pages = (total + limit - 1) // limit

    return {
        "items": paginated_books,
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
    }


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
