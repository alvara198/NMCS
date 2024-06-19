from Back_end.distributors import Distributors
from Back_end.Products import Products
import datetime
import time

class Sales:
    def __init__(self, distributor, product, units_sold, unic_code=int(time.time())):
        self._unic_code = unic_code
        self._distributor = None
        self.distributor = distributor
        date_time = datetime.datetime.fromtimestamp(unic_code)
        formatted_date = date_time.strftime('%Y-%m-%d %H:%M:%S')
        self._date = formatted_date
        self._product = None
        self.product = product
        self._units_sold = None
        self.units_sold = units_sold
        self._total_price = units_sold * product.product_unit_price

    @property
    def unic_code(self):
        return self._unic_code

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        if isinstance(value, Distributors):
            self._distributor = value
        else:
            raise TypeError("Distributor is not listed")

    @property
    def date(self):
        return self._date

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, value):
        if isinstance(value, Products):
            self._product = value
        else:
            raise ValueError("This product is not listed!")

    @property
    def units_sold(self):
        return self._units_sold

    @units_sold.setter
    def units_sold(self, value):
        if value < 1:
            raise ValueError("Units sold cannot be non-positive")
        self._units_sold = value

    @property
    def total_price(self):
        return self._total_price

    def __str__(self):
        return(
            f"{self.distributor.full_name()} sold {self.units_sold} {self.product.product_name}s. Total price was - {self.total_price}$"
        )
