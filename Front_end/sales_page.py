from tkinter import *
from datetime import datetime

def on_frame_configure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def sales_page(distributors, sales, products):
    from Front_end.new_sale_page import new_sale_page

    sales = sales
    distributors = distributors
    products = products

    root = Tk()
    root.title("Sales page")
    root.geometry("800x600")

    sales_list_frame = LabelFrame(root, padx=5, pady=5)
    canvas = Canvas(sales_list_frame)
    scrollbar = Scrollbar(sales_list_frame, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    sales_frame = Frame(canvas)

    sales_label = Label(root, text="Sales Made", anchor="w", font=("Arial", 32))
    home_page_button = Button(root, text="<-- Home page", width=20, padx=10, pady=10)
    new_sale_button = Button(root, text="New Sale", width=20, padx=10, pady=10, command=new_sale_page)
    refresh_button = Button(root, text="Refresh", width=20, padx=10, pady=10)

    sales_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    home_page_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    new_sale_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")
    refresh_button.grid(row=1, column=2, padx=10, pady=10, sticky="w")

    sales_list_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky="nsew")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    canvas.create_window((0, 0), window=sales_frame, anchor="nw")
    sales_frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

    for i, (key, value) in enumerate(sales.items()):
        date_of_sale = Label(sales_frame, text=f"{datetime.fromtimestamp(int(key))}", padx=10, anchor='w', font=("Arial", 16))
        distributor_of_sale = Label(sales_frame, text=value.distributor.full_name(), padx=10, font=("Arial", 16))
        product_of_sale = Label(sales_frame, text=value.product, padx=10, font=("Arial", 16))
        quantity_sold = Label(sales_frame, text=f"Unit price: {value.units_sold}", padx=10, font=("Arial", 16))
        total_price = Label(sales_frame, text=f"Total value: {value._total_price}", padx=10, font=("Arial",16), anchor="e")

        date_of_sale.grid(row=i, column=0, pady=5, sticky="w")
        distributor_of_sale.grid(row=i, column=1, pady=5, sticky="ew")
        product_of_sale.grid(row=i, column=2, pady=5, sticky="ew")
        quantity_sold.grid(row=i, column=3, pady=5, sticky="ew")
        total_price.grid(row=i, column=4, pady=5, sticky="e")

    sales_frame.grid_columnconfigure(index=0, weight=1)
    sales_frame.grid_columnconfigure(index=1, weight=1)
    sales_frame.grid_columnconfigure(index=2, weight=1)

    root.grid_columnconfigure(index=0, weight=1)
    root.grid_rowconfigure(index=2, weight=1)
    sales_list_frame.grid_rowconfigure(index=0, weight=1)
    sales_list_frame.grid_columnconfigure(index=0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    sales_page()