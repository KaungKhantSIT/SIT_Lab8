#Product classes
import math
from abc import ABC, abstractmethod
from typing import Any
from shipping import CanBeShipped
from supplier import Supplier

#Parent Product Class
class Product(ABC):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id: str = str(product_id).strip().upper()
        self.__name: str = str(name).strip()
        self.__price: float = self.__validate_price(price)
        self.__stock: int = self.__validate_stock(stock)
        self.__supplier: Supplier = supplier
        if not self.__product_id:
            raise ValueError("Product ID cannot be empty.")
        if not self.__name:
            raise ValueError("Name cannot be empty.")

    @staticmethod
    def __validate_price(price: float) -> float:
        if isinstance(price, bool):
            raise ValueError("Price must be a number")
        price = round(float(price), 2)
        if not math.isfinite(price):
            raise ValueError("Price must be a real number")
        if price <= 0:
            raise ValueError("Price must be more than $0")
        return price

    @staticmethod
    def __validate_stock(stock: int) -> int:
        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("Stock must be a whole number.")
        if stock < 0:
            raise ValueError("Stock must be 0 or higher.")
        return stock

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        self.__stock = self.__validate_stock(quantity)

    def display_info(self) -> None:
        print(f"ID: {self.__product_id}|Name: {self.__name}|"
              f"Price: ${self.__price:.2f}|Stock: {self.__stock}")
        self.__supplier.display_information()

    def to_dict(self) -> dict[str, str | float | int]:
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict[str, Any]) -> "Product":
        pass

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass

#Physical Product Class (inherits from Product)
class PhysicalProduct(Product, CanBeShipped):

    SHIPPING_BASE_FEE: float = 5.00
    SHIPPING_RATE_PER_KG: float = 2.50

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = self.__validate_weight(weight)

    @staticmethod
    def __validate_weight(weight: float) -> float:
        if isinstance(weight, bool):
            raise ValueError("Weight must be a number")
        weight = float(weight)
        if not math.isfinite(weight):
            raise ValueError("Weight must be a real number")
        if weight <= 0:
            raise ValueError("Weight must be more than 0 kg")
        return weight

    @property
    def weight(self) -> float:
        return self.__weight

    def display_info(self) -> None:
        super().display_info()
        print(f"Type: Physical|Weight: {self.__weight} kg\n")

    def get_fulfilment_info(self) -> str:
        return f"{self.name} is a physical product and requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return round(self.SHIPPING_BASE_FEE + self.__weight * self.SHIPPING_RATE_PER_KG, 2)

    def to_dict(self) -> dict[str, str | float | int]:
        data = super().to_dict()
        data["Type"] = "Physical"
        data["Weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "PhysicalProduct":
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Weight"])


#Digital Product Class (inherits from Product)
class DigitalProduct(Product):

    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, file_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__file_size: float = self.__validate_file_size(file_size)

    @staticmethod
    def __validate_file_size(file_size: float) -> float:
        if isinstance(file_size, bool):
            raise ValueError("File size must be a number")
        file_size = float(file_size)
        if not math.isfinite(file_size):
            raise ValueError("File size must be a real number")
        if file_size <= 0:
            raise ValueError("File size must be more than 0 MB")
        return file_size

    @property
    def file_size(self) -> float:
        return self.__file_size

    def display_info(self) -> None:
        super().display_info()
        print(f"Type: Digital|File Size: {self.__file_size} MB\n")

    def get_fulfilment_info(self) -> str:
        return f"{self.name} is a digital product and is delivered digitally via download."

    def to_dict(self) -> dict[str, str | float | int]:
        data = super().to_dict()
        data["Type"] = "Digital"
        data["File Size"] = self.__file_size
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DigitalProduct":
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["File Size"])


#Lookup Table
PRODUCT_TYPES: dict[str, type[Product]] = {
    "Physical": PhysicalProduct,
    "Digital": DigitalProduct
}