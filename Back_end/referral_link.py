"""""
class ReferralLink:
    referred_people = set()

    def __init__(self, distributor, referral = None, referrer = None):
       self._referrer = None
       self._distributor = None
       self._referral = []
       self.referral = referral
       self.referrer = referrer
       self.distributor = distributor

    @property
    def referrer(self):
        return self._referrer

    @referrer.setter
    def referrer(self, value):
            self._referrer = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        if value in ReferralLink.referred_people:
            raise ValueError("This person is already referral of another distributor!")
        else:
            if isinstance(value, Distributors):
                self._distributor = value
                ReferralLink.referred_people.add(value)
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
        elif value == None:
            self._referral = None
        else:
            raise TypeError("Refferal must be list type, up to 3 elements!")

    def add_referral(self, distributor):
        referrals = self.referral
        if distributor in ReferralLink.referred_people:
            raise ValueError("This person is already referred by another distributor!")
        else:
            if isinstance(distributor, Distributors) and len(referrals) <= 2:
                referrals.append(distributor)
                ReferralLink.referred_people.add(distributor)
            else:
                raise ValueError("Person you are trying to add to the referral link is not an distributor or too many distributors in a link!") #can come up with better error text

    def remove_referral(self, distributor):
        if not isinstance(distributor, Distributors):
            raise TypeError("object you are trying to remove is not even distributor!")
        if distributor in self.referral:
            self.referral.remove(distributor)
        else:
            raise ValueError("Distributor you are trying to remove is not part of the referral link")

    def __str__(self):
        return (
            f"{self.distributor.name} {self.distributor.last_name} is referred by {self.referrer.name} {self.referrer.last_name} "
        )

    def __repr__(self):
        return (
            f"{self.referrer} -> {self.distributor} -> {self.referral}"
        )
"""""
