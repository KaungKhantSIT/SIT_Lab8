from supplier import Supplier
from product import PhysicalProduct, DigitalProduct

supplier = Supplier("SUP-001", "Acme Supplies", "contact@acme.example")

physical_product = PhysicalProduct(
    "PHY-001", "Wireless Mouse", 24.99, 50, supplier, 0.25
)
digital_product = DigitalProduct(
    "DIG-001", "Design Software License", 49.99, 100, supplier, 250
)

print("Physical product:")
physical_product.display_info()

print("\nDigital product:")
digital_product.display_info()

print("\nDeleting\n")
del supplier

print("Physical product:")
physical_product.display_info()

print("\nDigital product:")
digital_product.display_info()