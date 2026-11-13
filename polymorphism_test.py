#Polymorphism test

from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory
 
supplier = Supplier("S001", "TechCo", "sales@techco.com")

products: list[Product] = [
    PhysicalProduct("P010", "Keyboard", 50.0, 10, supplier, 0.8),
    DigitalProduct("P011", "Antivirus", 29.99, 5, supplier, 200),
]

inventory = Inventory()
for product in products:
    inventory.add_product(product)
print("Products added to Inventory\n")

#inventory.display_all()

products[0].display_info()
print(products[0].get_fulfilment_info())

products[1].display_info()
print(products[1].get_fulfilment_info())