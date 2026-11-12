# Supplier Class

class Supplier:

    def __init__(self, supplier_id, name, contact_email):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def display_information(self):
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Name: {self.__name}")
        print(f"Contact Email: {self.__contact_email}")