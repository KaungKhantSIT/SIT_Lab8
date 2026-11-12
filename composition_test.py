from supplier import Supplier
from product import PhysicalProduct, DigitalProduct
from Order import Order
 
supplier = Supplier("S001", "TechCo", "sales@techco.com")
keyboard = PhysicalProduct("P010", "Keyboard", 50.0, 10, supplier, 0.8)
antivirus = DigitalProduct("P011", "Antivirus", 29.99, 5, supplier, 200)


order_1 = Order("O001")
order_1.add_order_line(keyboard, 2)
order_1.add_order_line(antivirus, 3)
order_1.display_order()


order_2 = Order("O002")
order_2.add_order_line(keyboard, 1)
order_2.display_order()

 
line_1 = order_1.order_lines[0]
line_2 = order_2.order_lines[0]

print(f"\nid() of O001's Keyboard line: {id(line_1)}")
print(f"id() of O002's Keyboard line: {id(line_2)}")

print(f"\nid() of O001 line.product: {id(line_1.product)}")
print(f"id() of O002 line.product: {id(line_2.product)}")


order_1.remove_order_line("P010")
order_1.display_order()

order_2.display_order()