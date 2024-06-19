import json
from Back_end.distributors import Distributors
from Back_end.Products import Products
from Back_end.address import Address
from Back_end.contact_information import ContactInformation
from Back_end.identity_information import IdentityInformation
from Back_end.sales import Sales
#from Back_end.referral_link import ReferralLink

class DataSaver:
        runtime_data = dict()
        products_runtime_data = dict()
        sales_runtime_data = dict()

        def to_runtime_data(item_to_be_saved):
                data_of_distributor = {
                        "name":item_to_be_saved.name,
                        "last_name":item_to_be_saved.last_name,
                        "gender":item_to_be_saved.gender,
                        "image":item_to_be_saved.image,
                        "date_of_birth":item_to_be_saved.date_of_birth,
                        "contact_information":{
                                "type":item_to_be_saved.contact_information.type,
                                "contact_information":item_to_be_saved.contact_information.contact_information
                        },
                        "identity_information":{
                                "Type": item_to_be_saved.identity_information.type,
                                "Date of Issue": item_to_be_saved.identity_information.date_of_issue,
                                "Date of Expiry": item_to_be_saved.identity_information.date_of_expiry,
                                "Personal Number": item_to_be_saved.identity_information.personal_number,
                                "Serie": item_to_be_saved.identity_information.serie,
                                "Card Number": item_to_be_saved.identity_information.card_number,
                                "Issuing Authority": item_to_be_saved.identity_information.issuing_authority
                        },
                        "address":{
                                "type": item_to_be_saved.address.type,
                                "address": item_to_be_saved.address.address
                        },
                        "referrer": None,
                        "referral": item_to_be_saved.referral
                }
                key_to_distributor = item_to_be_saved.distributor_code
                DataSaver.runtime_data[key_to_distributor] = data_of_distributor

        def create_distributor_from_runtime_data(distributor_code, data):
                contact_info = ContactInformation(
                        data[distributor_code]['contact_information']['type'],
                        data[distributor_code]['contact_information']['contact_information']
                )

                identity_info = IdentityInformation(
                        data[distributor_code]['identity_information']['Type'],
                        data[distributor_code]['identity_information']['Date of Issue'],
                        data[distributor_code]['identity_information']['Date of Expiry'],
                        data[distributor_code]['identity_information']['Personal Number'],
                        data[distributor_code]['identity_information'].get('Serie'),
                        data[distributor_code]['identity_information'].get('Card Number'),
                        data[distributor_code]['identity_information'].get('Issuing Authority')
                )

                address = Address(
                        data[distributor_code]['address']['type'],
                        data[distributor_code]['address']['address']
                )

                distributor = Distributors(
                        name=data[distributor_code]['name'],
                        last_name=data[distributor_code]['last_name'],
                        gender=data[distributor_code]['gender'],
                        image=data[distributor_code]['image'],
                        date_of_birth=data[distributor_code]['date_of_birth'],
                        contact_information=contact_info,
                        identity_information=identity_info,
                        address=address,
                        referrer=data[distributor_code]['referrer'],
                        referral=data[distributor_code]["referral"],
                        distributor_code=distributor_code
                )

                return distributor

        def transfer_data_to_json(dict_to_json, json_name):
                with open(json_name, 'w') as json_file:
                        json.dump(dict_to_json, json_file, indent=4)

        def transfer_data_from_json(json_name):
                with open(json_name, 'r') as json_file:
                        DataSaver.runtime_data = json.load(json_file)

        def transfer_products_from_json(json_name):
                with open(json_name, 'r') as json_file:
                        DataSaver.products_runtime_data = json.load(json_file)

        def transfer_sales_from_json(json_name):
                with open(json_name, 'r') as json_file:
                        DataSaver.sales_runtime_data = json.load(json_file)


        def to_product_runtime_data(product_to_be_saved):
                product_data = {
                        "product_name": product_to_be_saved.product_name,
                        "product_unit_price": product_to_be_saved.product_unit_price
                }
                key_to_product = product_to_be_saved.product_code
                DataSaver.products_runtime_data[key_to_product] = product_data

        def create_product_from_product_runtime_data(product_code, data):
                retrieved_product = Products(
                        product_code=product_code,
                        product_name=DataSaver.products_runtime_data[product_code]['product_name'],
                        product_unit_price=DataSaver.products_runtime_data[product_code]['product_unit_price']
                )
                return retrieved_product

        def to_sales_runtime_data(sale_to_be_saved):
                sale_data = {
                        "distributor": sale_to_be_saved.distributor.distributor_code,
                        "product": sale_to_be_saved.product.product_code,
                        "units_sold": sale_to_be_saved.units_sold
                }
                key_to_sale = sale_to_be_saved.unic_code
                DataSaver.sales_runtime_data[key_to_sale] = sale_data


        def get_sale_from_sales_runtime_data(sale_code, data):
                print(DataSaver.runtime_data.get(data[sale_code]["distributor"]))
                type(DataSaver.runtime_data.get(data[sale_code]["distributor"]))
                retrieved_sale = Sales(
                        distributor=DataSaver.runtime_data.get(data[sale_code]["distributor"]),
                        product=DataSaver.products_runtime_data.get(data[sale_code]["product"]),
                        units_sold=data[sale_code]["units_sold"],
                        unic_code= int(sale_code)
                )
                return retrieved_sale


