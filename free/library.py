class Library:
    def __init__(self):
        self.catalog = {}

    def add_book(self, title: str, author: str):
        if title in self.catalog:
            raise ValueError(f'Title "{title}" is already taken')
        self.catalog[title] = {"author": author}

    def remove_book(self, title: str):
        if title not in self.catalog:
            raise ValueError(f'Title "{title}" does not exist')
        del self.catalog[title]

    def find_book(self, title: str):
        if title in self.catalog:
            return f"Title: {title}, Author: {self.catalog[title]['author']}"
        return None

    def list_books(self):
        if not self.catalog:
            return "No books in the catalog"
        return "\n".join(
            [f"Title: {title}, Author: {info['author']}" for title, info in self.catalog.items()]
        )


