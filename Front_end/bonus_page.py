from tkinter import *
from datetime import datetime

import data.data_saver


def calculate_bonus(root, start_date, end_date, distributor):
    start_date = start_date.get()
    formated_start = (datetime.strptime(start_date, "%Y-%m-%d").timestamp())
    end_date = end_date.get()
    formated_end = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
    distributor_entry = distributor.get()
    bonus = 0
    for key, value in data.data_saver.DataSaver.sales_runtime_data.items():
        int_key = int(key)
        if formated_start < int_key < formated_end and value.distributor.distributor_code == distributor_entry:
            bonus += value._total_price*0.1
    view_bonus = Label(root, text=f"Distributor earned {bonus}$", padx=10, pady=10, font=("Arial", 16), anchor="w")
    view_bonus.grid(row=4, column=1, sticky="e")


def bonus_page(distributors, sales, products):
    distributors = distributors
    sales = sales
    products = products

    root = Tk()
    root.title("Bonus Page")
    root.geometry("800x400")

    # labels
    bonus_calculator_label = Label(root, text="Bonus Calculator", padx=10, pady=10, font=("Arial", 48), anchor="center")
    starting_date_label = Label(root, text="Start Date", padx=10, pady=10, anchor="center")
    ending_date_label = Label(root, text="End Date", padx=10, pady=10, anchor="center")
    distributor_label = Label(root, text="Distributor Code", padx=10, pady=10, anchor="center")

    # buttons
    home_page_button = Button(root, text="<-- Home page", width=20, padx=10, pady=10)
    calculate_bonus_button = Button(root, text="Calculate bonus:", width=30, padx=10, pady=10, command=lambda: calculate_bonus(root, start_date_entry, end_date_entry, distributor_code_entry))

    # entries
    start_date_entry = Entry(root, width=30)
    end_date_entry = Entry(root, width=30)
    distributor_code_entry = Entry(root, width=30)

    # putting stuff on screen
    home_page_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
    bonus_calculator_label.grid(row=1, column=0, columnspan=3, sticky="ew")
    starting_date_label.grid(row=2, column=0, sticky="ew")
    ending_date_label.grid(row=2, column=1, sticky="ew")
    distributor_label.grid(row=2, column=2, sticky="ew")
    calculate_bonus_button.grid(row=4, column=0, sticky="e", pady=100)
    start_date_entry.grid(row=3, column=0, sticky="ew", padx=10)
    end_date_entry.grid(row=3, column=1, sticky="ew", padx=10)
    distributor_code_entry.grid(row=3, column=2, sticky="ew", padx=10)

    root.grid_columnconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=1, weight=1)
    root.grid_columnconfigure(index=2, weight=1)

    root.mainloop()


if __name__ == "__main__":
    bonus_page()