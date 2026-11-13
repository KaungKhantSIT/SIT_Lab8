#Test for Liskov Substitution Principle

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

for product in products:
    inventory.find_product(product.product_id)

print(inventory.find_product("P010").name)
print(inventory.find_product("P011").name)