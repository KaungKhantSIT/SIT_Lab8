from supplier import Supplier
from product import PhysicalProduct
from inventory import Inventory
 
supplier = Supplier("S001", "TechCo", "sales@techco.com")
keyboard = PhysicalProduct("P010", "Keyboard", 50.0, 10, supplier, 0.8)
keyboard.display_info()
print("\nProduct Created")
 
inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(keyboard)
print(f"\nAdded product to inventory A")

removed = inventory_a.remove_product("P010")
print(f"\nRemoved product from inventory A")

keyboard.update_stock(15)
keyboard.display_info()
 
inventory_b.add_product(keyboard)
print(f"\nAdded product to inventory B")
 
inventory_b.remove_product("P010")
print(f"\nRemoved product from inventory B")

keyboard.display_info()