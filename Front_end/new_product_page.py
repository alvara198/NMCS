from tkinter import *

import data.data_saver
from Back_end.Products import Products
from data.data_saver import DataSaver

def save_product(name, price, code, product_runtime=dict()):
    name_ = str(name.get())
    name.delete(0, END)
    price_ = float(price.get())
    price.delete(0, END)
    code_ = str(code.get())
    code.delete(0, END)

    new_product = Products(product_name=name_, product_unit_price=price_, product_code=code_)
    product_runtime[new_product.product_code] = new_product
    for key, value in product_runtime.items():
        data.data_saver.DataSaver.to_product_runtime_data(value)
    data.data_saver.DataSaver.transfer_data_to_json(DataSaver.products_runtime_data, "data/products.json")

    print(data.data_saver.DataSaver.products_runtime_data)

def new_product_page():
    root = Tk()
    root.title("New Product Window")

    root.geometry("400x600")

    #labels
    title = Label(root, text="New Product", font=("Arial", 36))
    product_name_title = Label(root, text="New Product Name:", font=("Arial", 16))
    product_unit_price_title = Label(root, text="New Product Unit Price:", font=("Arial", 16))
    product_code_title = Label(root, text="New Product Code:", font=("Arial", 16))

    #entry fields
    name_entry = Entry(root, width=50)
    product_unit_price_entry = Entry(root, width=50)
    product_code_entry = Entry(root, width=50)


    #buttons
    save_button = Button(root, text="Save Product", width=15, command=lambda: save_product(name_entry, product_unit_price_entry, product_code_entry, product_runtime=DataSaver.products_runtime_data))
    cancel_button = Button(root, text="cancel", width=20, command=root.destroy)

    #putting stuff on a screen
    title.grid(row=0, column=0, padx=10, pady=20, columnspan=2, sticky="w")
    product_name_title.grid(row=1, column=0, padx=10, pady=10, sticky="nw", columnspan=2)
    name_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
    product_unit_price_title.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
    product_unit_price_entry.grid(row=5, column=0, padx=10, pady=10, sticky="nw")
    product_code_title.grid(row=6, column=0, padx=10, pady=10, sticky="nw")
    product_code_entry.grid(row=7, column=0, padx=10, pady=10, sticky="nw")
    save_button.grid(row=8, column=0, padx=10, pady=20, sticky="nw")
    cancel_button.grid(row=10, column=1, padx=10, pady=10, sticky="es")


    root.grid_rowconfigure(index=0, weight=0)
    root.grid_rowconfigure(index=1, weight=0)
    root.grid_rowconfigure(index=2, weight=0)
    root.grid_rowconfigure(index=10, weight=1)
    root.grid_columnconfigure(index=1, weight=1)
    root.grid_columnconfigure(index=0, weight=1)


    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    new_product_page()
