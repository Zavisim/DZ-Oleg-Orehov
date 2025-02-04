class Product:
    def __init__(self, id: int, name: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount: int):
        self.stock += amount

    def get_info(self):
        return {'id': self.id, 'name': self.name, 'price': self.price, 'stock': self.stock}


class User:
    def __init__(self, username: str, email: str, balance: float):
        self.username = username
        self.email = email
        self.balance = balance

    def add_balance(self, amount: float):
        self.balance += amount

    def get_info(self):
        return {'username': self.username, 'email': self.email, 'balance': self.balance}


class Order:
    def __init__(self, id: int, user: User):
        self.id = id
        self.user = user
        self.products = []
        self.status = "Pending"

    def add_product(self, product: Product, quantity: int):
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for product {product.name}")
        product.update_stock(-quantity)
        self.products.append((product, quantity))

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.products)

    def complete_order(self):
        total_cost = self.calculate_total()
        self.user.balance -= total_cost
        self.status = "Completed"

    def cancel_order(self):
        if self.status == "Completed":
            raise ValueError(f"Поздняк")
        for product, quantity in self.products:
            product.update_stock(quantity)
        self.status = "Canceled"

    def get_info(self):
        return f"Order {self.id} - Status: {self.status}, Total: {self.calculate_total()}"


class Shop:
    def __init__(self):
        self.products = []
        self.orders = []

    def add_product(self, product: Product):
        self.products.append(product)

    def find_product(self, product_id: int):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def create_order(self, user: User):
        order_id = len(self.orders) + 1
        order = Order(order_id, user)
        self.orders.append(order)
        return order

    def get_order(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None


if __name__ == "__main__":
    # Создаем магазин
    shop = Shop()

    # Добавляем товары
    product1 = Product(1, "Laptop", 1000, 10)
    product2 = Product(2, "Phone", 500, 20)
    shop.add_product(product1)
    shop.add_product(product2)

    # Создаем пользователя
    user = User("Alice", "alice@example.com", 1500)

    # Создаем заказ
    order = shop.create_order(user)
    order.add_product(product1, 1)
    order.add_product(product2, 2)

    # Завершаем заказ
    print(order.get_info())  # Order 1 - Status: Pending, Total: 2000
    order.complete_order()
    print(order.get_info())  # Order 1 - Status: Completed, Total: 2000

    # Вывод информации о пользователе
    print(user.get_info())  # User: Alice, Email: alice@example.com, Balance: -500

    # Отмена заказа (если статус "Pending")
    order.cancel_order()
