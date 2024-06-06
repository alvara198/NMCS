from Back_end.distributors import Distributors
from Back_end.Products import Products
from Back_end.address import Address
from Back_end.identity_information import IdentityInformation
from Back_end.contact_information import ContactInformation


address1 = Address("Formal", "st.johns 52")
identity_info1 = IdentityInformation(
    type="Passport",
    date_of_issue="2022-01-01",
    date_of_expiry="2032-01-01",
    personal_number="1234567890",
    serie="AB12345",
    card_number="7890123456",
    issuing_authority="Department of State"
)
contact_info_telephone = ContactInformation(
    type="Telephone#",
    contact_information="1234567890"
)

#print(f"address1 type - {type(address1)}")
# Create some distributors
distributor1 = Distributors("John", "Doe", "1990-01-01", "Male", "image1.jpg", contact_info_telephone, identity_info1, address1)
#distributor2 = Distributors("Jane", "Smith", "1985-05-15", "Female", "image2.jpg", "098-765-4321", "ID54321", "456 Elm St")

bananas = Products("21T@FSAA", "Banana", 3)



print(distributor1)  # Output includes Distributor Code
#print(distributor2)  # Output includes Distributor Code
#print(f"Total distributors: {Distributors.total_distributors}")  # Output should reflect the total distributors created
#print(bananas)

