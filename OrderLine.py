#Order Line Class
from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    def calculate_subtotal(self) -> float:
        subtotal = self.__product.price * self.__quantity
        return subtotal

    def display_info(self) -> None:
        print(f"Product: {self.__product.product_id} {self.__product.name}|"
              f"Qty: {self.__quantity}|Unit Price: ${self.__product.price:.2f}|"
              f"Subtotal: ${self.calculate_subtotal():.2f}")