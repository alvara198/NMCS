from Back_end.distributors import Distributors

class RefferalLink:
    def __init__(self, distributor, referrer = None):
       self._referrer = None
       self._distributor = None
       self._referral = []
       self.referrer = referrer
       self.distributor = distributor

    @property
    def referrer(self):
        return self._referrer

    @referrer.setter
    def referrer(self, value):
        if isinstance(value, Distributors):
            self._referrer = value
        else:
            raise TypeError("Refferer must be an existing distributor!")

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        if isinstance(value, Distributors):
            self._distributor = value
        else:
            raise TypeError("Distributor must be type Distributors!")

    @property
    def referral(self):
        return self._referral

    @referral.setter
    def referral(self, value):
        if isinstance(value, list):
            if len(value) < 4:
                self._referral = value
            else:
                raise ValueError("A Distributor can have up to 3 referrals!")
        else:
            raise TypeError("Refferal must be list type, up to 3 elements!")

    def add_referral(self, distributor):
        referrals = self.referral
        if isinstance(distributor, Distributors) and len(referrals) <= 3:
            referrals.append(distributor)
        else:
            raise ValueError("Person you are trying to add to the referral link is not an distributor or too many distributors in a link!") #can come up with better error text

    def remove_referral(self, distributor):
        if not isinstance(distributor, Distributors):
            raise TypeError("object you are trying to remove is not even distributor!")
        if distributor in self.referral:
            self.referral.remove(distributor)
        else:
            raise ValueError("Distributor you are trying to remove is not part of the referral link")
