from Back_end.identity_information import IdentityInformation
from Back_end.address import Address
from Back_end.contact_information import ContactInformation

class Distributors:
    total_distributors = 0

    def __init__(self, name, last_name, date_of_birth, gender, image, contact_information, identity_information, address):
        Distributors.total_distributors += 1
        self._name = None
        self.name = name
        self._last_name = None
        self.last_name = last_name
        self._date_of_birth = date_of_birth
        self._gender = None
        self.gender = gender
        self._image = image
        self._contact_information = None
        self.contact_information = contact_information
        self._identity_information = None
        self.identity_information = identity_information
        self._address = None
        self.address = address
        self._distributor_code = self.generate_distributor_code()


    @property
    def distributor_code(self):
        return self._distributor_code

    def generate_distributor_code(self):
        global total_distributors
        unic_code = f"000000000{Distributors.total_distributors}"
        return unic_code[-6:]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 50 and value.isalpha():
            self._name = value
        else:
            raise ValueError("Name must must contain only latin letters and be no longer than 50 characters!")


    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if len(value) <= 50 and value.isalpha():
            self._last_name = value
        else:
            raise ValueError("Last Name must must contain only latin letters and be no longer than 50 characters!")

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        self._date_of_birth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value == "Male" or value == "Female":
            self._gender = value
        else:
            raise ValueError("Gender must be either Male or Female!")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def contact_information(self):
        return self._contact_information

    @contact_information.setter
    def contact_information(self, value):
        if isinstance(value, ContactInformation):
            self._contact_information = value
        else:
            raise TypeError("Contact information type must be ContactInformation!")

    @property
    def identity_information(self):
        return self._identity_information

    @identity_information.setter
    def identity_information(self, value):
        if isinstance(value, IdentityInformation):
            self._identity_information = value
        else:
            raise TypeError("Identity information type must be IdentityInformation!")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if isinstance(value, Address):
            self._address = value
        else:
            raise TypeError("address type must be Address object!")


    def full_name(self):
        return f"{self.name} {self.last_name}"

    def contact_details(self):
        return f"Contact Information: {self.contact_information}"

    def identity_details(self):
        return f"Identity Information: {self.identity_information}"

    def address_details(self):
        return f"Address: {self.address}"

    def __str__(self):
        return (f"Distributor: {self.full_name()}\n"
                f"Date of Birth: {self.date_of_birth}\n"
                f"Gender: {self.gender}\n"
                f"{self.contact_details()}\n"
                f"{self.identity_details()}\n"
                f"{str(self.address)}\n"
                f"{self.distributor_code}")
