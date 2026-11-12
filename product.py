#Product classes
import math
from abc import ABC, abstractmethod
from shipping import CanBeShipped

#Parent Product Class
class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = str(product_id).strip().upper()
        self.__name = str(name).strip()
        self.__price = self.__validate_price(price)
        self.__stock = self.__validate_stock(stock)
        if not self.__product_id:
            raise ValueError("Product ID cannot be empty.")
        if not self.__name:
            raise ValueError("Name cannot be empty.")

    @staticmethod
    def __validate_price(price):
        if isinstance(price, bool):
            raise ValueError("Price must be a number")
        price = round(float(price), 2)
        if not math.isfinite(price):
            raise ValueError("Price must be a real number")
        if price <= 0:
            raise ValueError("Price must be more than $0")
        return price

    @staticmethod
    def __validate_stock(stock):
        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("Stock must be a whole number.")
        if stock < 0:
            raise ValueError("Stock must be 0 or higher.")
        return stock

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = self.__validate_stock(quantity)

    def display_info(self):
        print(f"ID: {self.__product_id}|Name: {self.__name}|"
              f"Price: ${self.__price:.2f}|Stock: {self.__stock}")

    def to_dict(self):
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass

    @abstractmethod
    def get_fulfilment_info(self):
        pass

#Physical Product Class (inherits from Product)
class PhysicalProduct(Product, CanBeShipped):

    SHIPPING_BASE_FEE = 5.00
    SHIPPING_RATE_PER_KG = 2.50

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = self.__validate_weight(weight)

    @staticmethod
    def __validate_weight(weight):
        if isinstance(weight, bool):
            raise ValueError("Weight must be a number")
        weight = float(weight)
        if not math.isfinite(weight):
            raise ValueError("Weight must be a real number")
        if weight <= 0:
            raise ValueError("Weight must be more than 0 kg")
        return weight

    @property
    def weight(self):
        return self.__weight

    def display_info(self):
        super().display_info()
        print(f"Type: Physical|Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return f"{self.name} is a physical product and requires physical shipping."

    def calculate_shipping_cost(self):
        return round(self.SHIPPING_BASE_FEE + self.__weight * self.SHIPPING_RATE_PER_KG, 2)

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "Physical"
        data["Weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Weight"])


#Digital Product Class (inherits from Product)
class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
        self.__file_size = self.__validate_file_size(file_size)

    @staticmethod
    def __validate_file_size(file_size):
        if isinstance(file_size, bool):
            raise ValueError("File size must be a number")
        file_size = float(file_size)
        if not math.isfinite(file_size):
            raise ValueError("File size must be a real number")
        if file_size <= 0:
            raise ValueError("File size must be more than 0 MB")
        return file_size

    @property
    def file_size(self):
        return self.__file_size

    def display_info(self):
        super().display_info()
        print(f"Type: Digital|File Size: {self.__file_size} MB")

    def get_fulfilment_info(self):
        return f"{self.name} is a digital product and is delivered digitally via download."

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "Digital"
        data["File Size"] = self.__file_size
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["File Size"])


#Lookup Table
PRODUCT_TYPES = {
    "Physical": PhysicalProduct,
    "Digital": DigitalProduct
}