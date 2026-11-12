#Order class
from OrderLine import OrderLine
from product import Product

class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        product_id = product_id.strip().upper()
        for line in self.order_lines:
            if line.product.product_id == product_id:
                self.order_lines.remove(line)
                return
            raise ValueError(f"No order line for product {product_id} in order {self.order_id}.")

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.order_lines:
            total += line.calculate_subtotal()
        return total

    def display_order(self) -> None:
        print(f"\nOrder {self.order_id}")
        print("-------------------------------------------")
        if not self.order_lines:
            print("No items in this order.")
        for line in self.order_lines:
            line.display_info()
        print("-------------------------------------------")
        print(f"Total: ${self.calculate_total():.2f}")