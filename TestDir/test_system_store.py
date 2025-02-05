import pytest
from free.SystemStore import Product, User, Order, Shop


@pytest.fixture
def shop() -> Shop:
    return Shop()


@pytest.fixture
def product1(shop: Shop) -> Product:
    return Product(1, "Laptop", 1000, 10)


@pytest.fixture
def product2(shop: Shop) -> Product:
    return Product(2, "phone", 500, 20)


@pytest.fixture
def user(shop: Shop) -> User:
    return User("Alice", "alice@example.com", 1500)


class TestSystemStore:
    def test_product1(self, product1: Product) -> None:
        assert product1.name == "Laptop"
        assert product1.price == 1000
        assert product1.stock == 10

    def test_product2(self, product2: Product) -> None:
        assert product2.name == "phone"
        assert product2.price == 500
        assert product2.stock == 20

    def test_user(self, user: User) -> None:
        assert user.username == "Alice"
        assert user.balance == 1500

    def test_add_product_order(self, shop, user, product1):
        order = shop.create_order(user)
        order.add_product(product1, 1)
        assert len(order.products) == 1
        assert product1.stock == 9

    def test_order_calculation(self, shop, user, product1, product2):
        order = shop.create_order(user)
        order.add_product(product1, 1)
        order.add_product(product2, 2)
        assert order.calculate_total() == 2000

    def test_order_complete(self, shop, user, product1):
        order = shop.create_order(user)
        order.add_product(product1, 1)
        order.complete_order()
        assert order.status == "Completed"
        assert product1.stock == 9

    def test_order_cancel(self, shop, user, product1):
        order = shop.create_order(user)
        order.add_product(product1, 1)
        order.cancel_order()
        assert order.status == "Canceled"
        assert product1.stock == 10

    def test_negative_balance(self, shop, user, product1, product2):
        order = shop.create_order(user)
        order.add_product(product1, 2)
        order.add_product(product2, 3)
        with pytest.raises(ValueError):
            order.complete_order()




