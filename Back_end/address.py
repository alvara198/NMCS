class Address:
    def __init__(self, type, address):
        self._type = None
        self._address = None
        self.type = type
        self.address = address

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value == "Actual" or value == "Formal":
            self._type = value
        else:
            raise ValueError("type of address must be either Actual or Formal!")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if len(value) <= 100:
            self._address = value
        else:
            raise ValueError("Address must contain no more than 100 characters!")

    def __str__(self):
        return(
            f"{self.type} address of this distributor is {self.address}."
        )
