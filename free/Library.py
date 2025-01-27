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

    def get_book(self, title: str):
        if title in self.catalog:
            return self.catalog[title]
        return None

    def list_books(self):
        if not self.catalog:
            return "No books in the catalog"
        return "\n".join(
            [f"Title: {title}, Author: {info['author']}" for title, info in self.catalog.items()]
        )


@pytest.fixture
def library() -> Library:
    return Library()


class TestLibrary:
    def test_add_book(self, library: Library):
        library.add_book("Book1", "Author1")
        """Пытался сделать через один assert, не уверен, что получилось лучше"""
        assert (
                "1984" in library.catalog and
                library.catalog["1984"] == {"author": "George Orwell"}
        )

    def test_add_replace_book(self, library: Library):
        """Подсмотрел жоско, как сделать проверку, на ValueError"""
        library.add_book("Book1", "Author1")
        with pytest.raises(ValueError):
            library.add_book("Book1", "Author1")

    def test_remove_book(self, library: Library):
        library.add_book("Book1", "Author1")
        library.remove_book("Book1")
        assert 'Book1' not in library.catalog

    def test_remove_book_not_exist(self, library: Library):
        """Тестируем удаление того, чего нет"""
        with pytest.raises(ValueError):
            library.remove_book("Trash")

    def test_get_book(self, library: Library):
        library.add_book("Book1", "Author1")
        result = library.get_book("Book1")
        assert result == "Title: Book1, Author: Author1"

    def test_get_book_not_exist(self, library: Library):
        result = library.get_book("Trash")
        assert result is None

    def test_list_books(self, library: Library):
        library.add_book("Book1", "Author1")
        library.add_book("Book2", "Author2")
        result = library.list_books()
        assert result == (
            """Title: Book1, Author: Author1\n TitTitle: Book1, Author: Author1"""
        )

    def test_list_books_not_exist(self, library: Library):
        result = library.list_books()
        assert result == "No books in the catalog"
