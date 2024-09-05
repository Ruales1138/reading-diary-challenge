from datetime import datetime

# TODO: Add code here


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.title: str = title
        self.author: str = author
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        self.notes: list[Note] = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        else:
            note = Note(text, page, date)
            self.notes.append(note)
            return True

    def set_rating(self, rating: int) -> bool:
        if rating != Book.EXCELLENT and rating != Book.GOOD and rating != Book.BAD:
            return False
        else:
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> list[Note]:
        return self.notes

    def page_with_most_notes(self) -> int:
        pass

    def __str__(self) -> str:
        return f"ISBN: {self.isbn} Title: {self.title} Author: {self.author} Pages: {self.pages} Rating: {self.rating}"




prueba = Book('s', 'jaja', 'david', 3)
prueba.add_note('sadsgf', 1, 28)
print(prueba.page_with_most_notes())

