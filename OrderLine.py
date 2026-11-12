#Order Line Class
from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product = product
        self.__quantity = quantity

    def calculate_subtotal(self) -> float:
        subtotal = self.__product.price * self.__quantity
        return subtotal