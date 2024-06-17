from tkinter import *

import data.data_saver


def home_page():
    from Front_end.products_page import products_page
    from Front_end.distributors_page import distributors_page

    root = Tk()
    root.title("Network Marketing Control System")

    root.geometry("800x600")

    WIDTH = 40

    label_home_page = Label(root, text="Home Page", font=("Arial", 16))

    button_developers = Button(root, text="Developers", width=WIDTH, pady=20, command=lambda: distributors_page())
    button_products = Button(root, text="Products", width=WIDTH, pady=20, command=lambda: products_page(data.data_saver.DataSaver.products_runtime_data))
    button_sales = Button(root, text="Sales", width=WIDTH, pady=20)
    button_bonus = Button(root, text="Bonus", width=WIDTH, pady=20)


    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=0)
    root.grid_columnconfigure(2, weight=1)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(6, weight=1)

    label_home_page.grid(row=1, column=1, pady=10)
    button_developers.grid(row = 2, column=1, pady=3)
    button_products.grid(row = 3, column=1, pady=3)
    button_sales.grid(row = 4, column=1, pady=3)
    button_bonus.grid(row = 5, column=1, pady=3)

    root.mainloop()

if __name__ == "__main__":
    home_page()
