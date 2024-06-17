from Back_end.referral_link import ReferralLink
from Back_end.distributors import Distributors

class LayeredReferralLink:
   def __init__(self, distributor):
      self._distributor = None
      self.distributor = distributor
      