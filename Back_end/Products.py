class Products:
    def __init__(self, product_code, product_name, product_unit_price):
        self._product_code = product_code
        self._product_name = product_name
        self._product_unit_price = product_unit_price

    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value

    @property
    def product_unit_price(self):
        return self._product_unit_price

    @product_unit_price.setter
    def product_unit_price(self, value):
        if type(value) != float:
            raise ValueError("Must be float!")
        self._product_unit_price = value

    def __str__(self):
        return (f"\nProduct code: {self._product_code}"
                f"\nProduct name: {self._product_name}"
                f"\nProduct unit price: {self._product_unit_price}$")
