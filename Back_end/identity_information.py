class IdentityInformation:
    def __init__(self, type, date_of_issue, date_of_expiry, personal_number, serie=None, card_number=None, issuing_authority=None):
        self._type = type
        self._date_of_issue = date_of_issue
        self._date_of_expiry = date_of_expiry
        self._personal_number = None
        self.personal_number = personal_number
        self._serie = serie
        self.serie = serie
        self._card_number = card_number
        self._issuing_authority = issuing_authority
        self.issuing_authority = issuing_authority

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,  value):
        self._type = value

    @property
    def date_of_issue(self):
        return self._date_of_issue

    @date_of_issue.setter
    def date_of_issue(self, value):
        self._date_of_issue = value

    @property
    def date_of_expiry(self):
        return self._date_of_expiry

    @date_of_expiry.setter
    def date_of_expiry(self, value):
        self._date_of_expiry = value

    @property
    def personal_number(self):
        return self._personal_number

    @personal_number.setter
    def personal_number(self, value):
        if value.isdigit() and len(value) <= 50:
            self._personal_number = value
        else:
            raise ValueError("Personal number must contain only digits and its length must be no longer than 50!")

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, value):
        if value == None:
            self._serie = value
        else:
            if len(value) > 10:
                raise ValueError("serie must be no longer than 10!")
            self._serie = value

    @property
    def card_number(self):
        return self._card_number

    @card_number.setter
    def card_number(self, value):
        self._card_number = value

    @property
    def issuing_authority(self):
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, value):
        if value == None:
            self._issuing_authority = value
        else:
            if len(value) > 100:
                raise ValueError("Name of the issuing authority is too big(max 100 characters)")
            self._issuing_authority = value

    def __str__(self):
        return (f"\n"
                f"Type: {self.type}\n"
                f"Date of Issue: {self.date_of_issue}\n"
                f"Date of Expiry: {self.date_of_expiry}\n"
                f"Personal Number: {self.personal_number}\n"
                f"Serie: {self.serie}\n"
                f"Card Number: {self.card_number}\n"
                f"Issuing Authority: {self.issuing_authority}\n")


