#Shipping interface
from abc import ABC, abstractmethod

class CanBeShipped(ABC):

    #Any class that implements this interface must provide a way to calculate shipping costs
    @abstractmethod
    def calculate_shipping_cost(self):
        pass