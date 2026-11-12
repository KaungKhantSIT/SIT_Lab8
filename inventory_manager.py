#Main Program

import json
import math
import re

from product import PRODUCT_TYPES, PhysicalProduct, DigitalProduct
from inventory import Inventory

#Convert text to a non-negative int
def parse_qty(raw):
    try:
        qty = int(raw)
    except ValueError:
        raise ValueError("Please enter a valid number.")
    if qty < 0:
        raise ValueError("Please enter a non-negative number.")
    return qty

#Check product ID format
def parse_id(raw,format=re.compile(r"P[0-9]{3,}")):
    pid = raw.upper()
    if not format.fullmatch(pid):
        raise ValueError("Please enter a valid product ID (e.g. P001).")
    return pid

#Convert text to a float above 0 (used for price, weight and download size)
def parse_positive(raw, decimals=None):
    try:
        value = float(raw)
    except ValueError:
        raise ValueError("Please enter a valid number.")
    if not math.isfinite(value):
        raise ValueError("Please enter a real number.")
    if decimals is not None:
        value = round(value, decimals)
    if value <= 0:
        raise ValueError("Please enter a number above 0.")
    return value

#Parse product type user input into corresponding class (PhysicalProduct or DigitalProduct)
def parse_type(raw):
    product_class = PRODUCT_TYPES.get(raw.capitalize())
    if product_class is None:
        raise ValueError(f"Please enter one of: {', '.join(PRODUCT_TYPES).lower()}.")
    return product_class

#Prompt until input is validated using required parse function
def prompt_until_valid(prompt, parse):
    while True:
        raw = input(prompt).strip()
        try:
            return parse(raw)
        except ValueError as err:
            print(err)

#Load inventory from json file
def load_inventory(filename):
    inventory = Inventory()
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"{filename} found.")
    #Empty inventory if file not found
    except (FileNotFoundError, json.JSONDecodeError, OSError) as err:
        print(f"Could not read {filename} ({err}). Starting with an empty inventory.\n")
        return inventory
    for item in data:
        try:
            product_class = PRODUCT_TYPES.get(item.get("Type"))
            if product_class is None:
                raise ValueError(f"Unknown product type: {item.get('Type')}")
            parse_id(str(item["ID"]).strip())
            inventory.add_product(product_class.from_dict(item))
        except KeyError as err:
            print(f"Skipped invalid record {item}: missing field {err}")
        except (ValueError, TypeError) as err:
            print(f"Skipped invalid record {item}: {err}")
    print("Inventory loaded successfully.\n")
    return inventory

#Save inventory to json file
def save_inventory(filename, inventory):
    print("\nSaving inventory...")
    try:
        with open(filename, 'w') as file:
            json.dump([product.to_dict() for product in inventory.get_products()], file, indent=4)
        print(f"Inventory saved successfully to {filename}.")
    except OSError as err:
        print(f"Could not save inventory: {err}")
    
#Ask the user for a new product's details and return the product object
def prompt_new_product(inventory):

    print("\nAdd New Product")

    #ID must match the format and not already be used
    pid = prompt_until_valid("Product ID: ", lambda raw: inventory.check_new_id(parse_id(raw)))

    #Name must not be empty or already used (Inventory.check_new_name)
    name = prompt_until_valid("Product Name: ", inventory.check_new_name)

    #Prompt for price & stock
    price = prompt_until_valid("Price($): ", lambda raw: parse_positive(raw, decimals=2))
    stock = prompt_until_valid("Stock Quantity: ", parse_qty)

    #Choose product type, then ask for the extra attribute that type needs
    product_class = prompt_until_valid("Type (physical/digital): ", parse_type)

    if product_class is PhysicalProduct:
        weight = prompt_until_valid("Weight (kg): ", parse_positive)
        return PhysicalProduct(pid, name, price, stock, weight)
    
    file_size = prompt_until_valid("Download Size (MB): ", parse_positive)
    return DigitalProduct(pid, name, price, stock, file_size)

#Prompt for an existing product ID and return it
def prompt_existing_id(inventory):
    pid = prompt_until_valid("Enter Product ID: ", parse_id)
    inventory.search_product(pid)
    return pid

#print menu options
def menu_page(menu):
    print("---------MENU---------")
    for i, option in enumerate(menu.keys(), start=1):
        print(f"{i}. {option}")
    print("----------------------\n")
    while True:
        option = input(f"Enter option (1-{len(menu)}): ").strip()
        if option.isdigit() and 1 <= int(option) <= len(menu):
            return list(menu.keys())[int(option) - 1]
        else:
            print("Invalid option. Please select a valid option.")

#Manager main program function
def manager():
    file = "inventory.json"
    #Title
    print("============================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("============================\n")
    # Load inventory from file
    inventory = load_inventory(file)
    #User menu options
    menu = {
        "Display All Products": (inventory.display_all, None),
        "Add New Product": (
            lambda: inventory.add_product(prompt_new_product(inventory)), "Product added successfully!"),
        "Update Stock": (
            lambda: inventory.update_stock(
                prompt_existing_id(inventory),
                prompt_until_valid("New Stock Quantity: ", parse_qty)),
            "Stock updated successfully!"),
        "Search Product": (
            lambda: inventory.display_product(prompt_until_valid("Enter Product ID: ", parse_id)), None),
        "Save Inventory": (
            lambda: save_inventory(file, inventory), None),
        "Exit": (None, None)
    }
    #Menu
    try:
        while True:
            option = menu_page(menu)
            if option == "Exit":
                break
            #Errors raised by Inventory methods (e.g. "Product Not Found") are shown instead of crashing
            action, success_message = menu[option]
            try:
                action()
                if success_message:
                    print(f"\n{success_message}")
            except ValueError as err:
                print(f"\n{err}")
            input("\nPress Enter to return to the menu...")
    except (KeyboardInterrupt, EOFError):
        print("\n\nInput interrupted.")
    save_inventory(file, inventory)
    print("\nThank you for using the Inventory Management System.")
    print("Program terminated.")
    
#Run main program
if __name__ == "__main__":
    manager()