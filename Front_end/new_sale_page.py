from tkinter import *
from Back_end.Products import Products
from Back_end.distributors import Distributors
from Back_end.sales import Sales
import data.data_saver
from data.data_saver import DataSaver
import json


def save_sale(distributor, product, units_sold):
    distributors = data.data_saver.DataSaver.runtime_data
    products = data.data_saver.DataSaver.products_runtime_data
    temp_sales = data.data_saver.DataSaver.sales_runtime_data
    distributor = distributors[distributor.get()]
    product = products[product.get()]
    units_sold = int(units_sold.get())
    new_sale = Sales(distributor=distributor, product=product, units_sold=units_sold)
    temp_sales[new_sale.unic_code]=new_sale
    data.data_saver.DataSaver.sales_runtime_data = {}
    for key, value in temp_sales.items():
        data.data_saver.DataSaver.to_sales_runtime_data(value)
    data.data_saver.DataSaver.transfer_data_to_json(data.data_saver.DataSaver.sales_runtime_data, "data/sales.json")
    print(data.data_saver.DataSaver.sales_runtime_data)

    for key, value in data.data_saver.DataSaver.sales_runtime_data.items():
        data.data_saver.DataSaver.sales_runtime_data[key] = data.data_saver.DataSaver.get_sale_from_sales_runtime_data(key, data.data_saver.DataSaver.sales_runtime_data)
    print(data.data_saver.DataSaver.sales_runtime_data)


def new_sale_page():

    root = Tk()
    root.title("New Sale Window")
    root.geometry("400x500")

    # Labels
    title = Label(root, text="New Sale", font=("Arial", 36))
    distributor_title = Label(root, text="Distributor Code:", font=("Arial", 16))
    product_title = Label(root, text="Product Code:", font=("Arial", 16))
    units_sold_title = Label(root, text="Units Sold:", font=("Arial", 16))

    # Entry Fields
    distributor_entry = Entry(root, width=50)
    product_entry = Entry(root, width=50)
    units_sold_entry = Entry(root, width=50)

    # Buttons
    save_button = Button(root, text="Save Sale", width=15, command=lambda: save_sale(distributor_entry, product_entry, units_sold_entry))
    cancel_button = Button(root, text="Cancel", width=20, command=root.destroy)

    # Placing Widgets
    title.grid(row=0, column=0, padx=10, pady=20, columnspan=2, sticky="w")
    distributor_title.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
    distributor_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
    product_title.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
    product_entry.grid(row=4, column=0, padx=10, pady=10, sticky="nw")
    units_sold_title.grid(row=5, column=0, padx=10, pady=10, sticky="nw")
    units_sold_entry.grid(row=6, column=0, padx=10, pady=10, sticky="nw")
    save_button.grid(row=7, column=0, padx=10, pady=20, sticky="nw")
    cancel_button.grid(row=7, column=1, padx=10, pady=20, sticky="nw")

    root.grid_rowconfigure(index=0, weight=0)
    root.grid_rowconfigure(index=1, weight=0)
    root.grid_rowconfigure(index=7, weight=1)
    root.grid_columnconfigure(index=1, weight=1)
    root.grid_columnconfigure(index=0, weight=1)

    # root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    new_sale_page()