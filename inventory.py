#Inventory class
from product import Product

class Inventory:

    def __init__(self) -> None:
        self.__products: list[Product] = []

    #Add new product
    def add_product(self, product: Product) -> None:
        self.check_new_id(product.product_id)
        self.check_new_name(product.name)
        self.__products.append(product)

    #Remove a product by ID
    def remove_product(self, product_id: str) -> Product:
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product Not Found")
        self.__products.remove(product)
        return product

    #Check that a product ID is not already in use
    def check_new_id(self, product_id: str) -> str:
        product_id = product_id.strip().upper()
        if any(p.product_id == product_id for p in self.__products):
            raise ValueError("Product ID already exists. Please enter a unique ID.")
        return product_id

    #Check that a product name is not empty and not already in use
    def check_new_name(self, name: str) -> str:
        name = name.strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        if self.find_by_name(name) is not None:
            raise ValueError("Product name already exists. Please enter a unique name.")
        return name

    #Search for product by id
    def find_product(self, product_id: str) -> Product | None:
        product_id = product_id.strip().upper()
        product = next((p for p in self.__products if p.product_id == product_id), None)
        return product

    #Search for product by name (case-insensitive)
    def find_by_name(self, name: str) -> Product | None:           
        name = name.strip().lower()
        return next((p for p in self.__products if p.name.lower() == name), None)

    #Update the stock of an existing product
    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product Not Found")
        product.update_stock(quantity)

    #Show a single product, found by ID
    def display_product(self, product_id: str) -> None:
        product = self.find_product(product_id)
        if product is None:
            raise ValueError("Product Not Found")
        print("\nProduct Found")
        print("-------------------------------------------")
        product.display_info()
        print(product.get_fulfilment_info())
        print("-------------------------------------------")

    #Show full inventory
    def display_all(self) -> None:          
        print("\nCurrent Inventory")
        print("-------------------------------------------")
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_info()
        print("-------------------------------------------")

    def get_products(self) -> list[Product]:
        return list(self.__products)

    def __len__(self) -> int:
        return len(self.__products)