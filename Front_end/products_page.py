from tkinter import *
import json
import os
import data.data_saver
from data.data_saver import DataSaver
from Back_end.Products import Products
from Back_end.distributors import Distributors
from Back_end.Products import Products
from Back_end.address import Address
from Back_end.contact_information import ContactInformation
from Back_end.identity_information import IdentityInformation
from Back_end.sales import Sales
from Front_end.home_page import home_page
from Front_end.new_product_page import save_product, new_product_page


def refresh_canvas(memory, product_frame, canvas):
    print(memory)
    for widget in product_frame.winfo_children():
        widget.destroy()


    i = 0
     #Add some products to the frame
    for code, product in memory.items():
        product_name = Label(product_frame, text=product.get("product_name"), padx=1, anchor='w', font=("Arial", 16))
        product_unit_price = Label(product_frame, text=str(product.get("product_unit_price"))+"$", padx=1, font=("Arial", 16))
        product_code = Label(product_frame, text=code, padx=1, font=("Arial", 16), anchor="e")
        product_name.grid(row=i, column=0, padx=(10, 50), pady=5, sticky="w")
        product_unit_price.grid(row=i, column=1, padx=(50, 50), pady=5,  sticky="ew")
        product_code.grid(row=i, column=2, padx=(50,10), pady=5, sticky="e")
        i += 1


    # Update the scroll region of the canvas
    product_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def products_page(memory):

   # products_dict= memory

    root = Tk()
    root.title("Products Page")
    root.geometry("800x600")

    # Create a product list frame that contains a canvas and a scrollbar
    product_list_frame = LabelFrame(root, padx=5, pady=5)
    canvas = Canvas(product_list_frame)
    scrollbar = Scrollbar(product_list_frame, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    product_frame = Frame(canvas)


    i = 0
    #Add some products to the frame
    for code, product in memory.items():
        product_ = memory[code]
        product_name = Label(product_frame, text=product_.product_name, padx=1, anchor='w', font=("Arial", 16))
        product_unit_price = Label(product_frame, text=str(product_.product_unit_price)+"$", padx=1, font=("Arial", 16))
        product_code = Label(product_frame, text=code, padx=1, font=("Arial", 16), anchor="e")
        product_name.grid(row=i, column=0, padx=(10, 50), pady=5, sticky="w")
        product_unit_price.grid(row=i, column=1, padx=(50, 50), pady=5,  sticky="ew")
        product_code.grid(row=i, column=2, padx=(50,10), pady=5, sticky="e")
        i += 1

    product_frame.grid_columnconfigure(index = 0, weight=1, uniform="col")
    product_frame.grid_columnconfigure(index = 1, weight=1, uniform="col")
    product_frame.grid_columnconfigure(index = 2, weight=1, uniform="col")

    # Create window inside the canvas
    canvas.create_window((0, 0), window=product_frame, anchor='center')

    # Update the scroll region of the canvas
    product_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Labels
    products_label = Label(root, text="Products", bd=1, font=("Arial", 24), padx=1, anchor='w')

    # Buttons
    back_to_home_page = Button(root, text="<--- Home page", width=20, pady=10, command=home_page)
    add_product_button = Button(root, text="New Product!", width=20, padx=40, pady=10, command=new_product_page)
    refresh_list_button = Button(root, text="Refresh List!", width=20, padx=40, pady=10, command=lambda: refresh_canvas(memory, product_frame, canvas))

    # Grid configuration
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=0)
    root.grid_rowconfigure(index=0, weight=0)
    root.grid_rowconfigure(index=1, weight=0)
    root.grid_rowconfigure(index=2, weight=1)
    product_list_frame.grid_rowconfigure(index=0, weight=1)
    product_list_frame.grid_columnconfigure(index=0, weight=1)



    # Putting stuff on screen
    back_to_home_page.grid(row=0, column=0, padx=5, pady=10)
    products_label.grid(row=1, column=0, padx=10, pady=10)
    add_product_button.grid(row=1, column=2, padx=10, pady=10)
    refresh_list_button.grid(row=1, column=3, padx=10, pady=10)
    product_list_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky="nsew")

    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=4, sticky="ns")

    root.mainloop()

if __name__ == "__main__":
    products_page()