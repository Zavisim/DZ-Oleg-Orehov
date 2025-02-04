import pytest
from free.library import Library


@pytest.fixture
def library() -> Library:
    return Library()


class TestLibrary:
    def test_add_book(self, library: Library):
        """Тест добавления книги"""
        library.add_book("Book1", "Author1")
        assert (
            "Book1" in library.catalog and
            library.catalog["Book1"] == {"author": "Author1"}
        )

    def test_add_replace_book(self, library: Library):
        """Проверка на повтор"""
        library.add_book("Book1", "Author1")
        with pytest.raises(ValueError):
            library.add_book("Book1", "Author1")

    def test_remove_book(self, library: Library):
        """Тест удаления"""
        library.add_book("Book1", "Author1")
        library.remove_book("Book1")
        assert "Book1" not in library.catalog

    def test_remove_book_not_exist(self, library: Library):
        """Тест удаления того, чего нет"""
        with pytest.raises(ValueError):
            library.remove_book("Trash")

    def test_find_book(self, library: Library):
        """Тест поиска книги по названия"""
        library.add_book("Book1", "Author1")
        result = library.find_book("Book1")
        assert result == "Title: Book1, Author: Author1"

    def test_find_book_not_exist(self, library: Library):
        """Тест поиска книги, которой нет"""
        result = library.find_book("Trash")
        assert result is None

    def test_list_books(self, library: Library):
        """Тест списка книг в каталоге"""
        library.add_book("Book1", "Author1")
        library.add_book("Book2", "Author2")
        result = library.list_books()
        assert result == "Title: Book1, Author: Author1\nTitle: Book2, Author: Author2"

    def test_list_books_not_exist(self, library: Library):
        """Тестируем пустой каталог"""
        result = library.list_books()
        assert result == "No books in the catalog"
