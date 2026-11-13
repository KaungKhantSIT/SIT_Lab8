# Supplier Class
from typing import Any
class Supplier:

    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Name: {self.__name}")
        print(f"Contact Email: {self.__contact_email}")

    def to_dict(self) -> dict[str, str]:
        return {
            "ID": self.__supplier_id,
            "Name": self.__name,
            "Contact Email": self.__contact_email
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "Supplier":
        if data is None:
            return cls("S000", "Unknown", "N/A")
        return cls(data["ID"], data["Name"], data["Contact Email"])