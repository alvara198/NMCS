import data.data_saver
from Back_end.distributors import Distributors
from Back_end.Products import Products
from Back_end.address import Address
from Back_end.identity_information import IdentityInformation
from Back_end.contact_information import ContactInformation
#from Back_end.referral_link import ReferralLink
from Back_end.sales import Sales
from data import data_saver
from Front_end.products_page import products_page, refresh_canvas
from Front_end.home_page import home_page
import tkinter
import datetime


data_saver.DataSaver.transfer_products_from_json("data/products.json")
print(data_saver.DataSaver.products_runtime_data)

data_saver.DataSaver.transfer_sales_from_json("data/sales.json")
print(data_saver.DataSaver.sales_runtime_data)


for key, value in data_saver.DataSaver.products_runtime_data.items():
    data_saver.DataSaver.products_runtime_data[key] = data.data_saver.DataSaver.create_product_from_product_runtime_data(key, data_saver.DataSaver.products_runtime_data)
print(data_saver.DataSaver.products_runtime_data)

data_saver.DataSaver.transfer_data_from_json("data/distributors.json")
print(data_saver.DataSaver.runtime_data)

print(data_saver.DataSaver.products_runtime_data)
#products_page(data_saver.DataSaver.products_runtime_data)
home_page()