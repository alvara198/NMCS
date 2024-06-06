class ContactInformation:
    def __init__(self, type, contact_information):
        self._type = None
        self._contact_information = None
        self.type = type
        self.contact_information = contact_information

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value == "Telephone#" or value == "E-mail":
            self._type = value
        else:
            raise ValueError("Type of contact information must be either phone number or E=mail!")

    @property
    def contact_information(self):
        return self._contact_information

    @contact_information.setter
    def contact_information(self, value):
        if self.type == "Telephone#":
            if value.isdigit() and len(value) < 101:
                self._contact_information = value
            else:
                raise ValueError("Telephone number must contain only digits and must be no longer that 100 characters!")
        elif self.type == "E-mail":
            if len(value) > 100:
                raise ValueError("Email must be no longer than 100 charachers")
            if value.count("@") != 1 or value.count(".") != 1:
                raise ValueError("Incorrect E-mail!")
            self._contact_information = value

    def __str__(self):
        return (
            f"{self.type} - {self.contact_information}"
        )
