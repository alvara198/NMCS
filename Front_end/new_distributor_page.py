from tkinter import *
from tkinter import filedialog

import data.data_saver
from Back_end.address import Address
from Back_end.contact_information import ContactInformation
from Back_end.identity_information import IdentityInformation
from Back_end.Products import Products
from Back_end.distributors import Distributors
from data.data_saver import DataSaver


def save_user(name, last_name, gender, image, dob, contact_type, contact_info, id_type, id_issue, id_expiry, id_pnum, id_series, id_cnum, id_authority, addr_type, addr):
    new_address = Address(type=addr_type.get(), address=addr.get())
    new_id = IdentityInformation(type=id_type.get(), date_of_issue=id_issue.get(), date_of_expiry=id_expiry.get(), personal_number=id_pnum.get(), serie=id_series.get(), card_number=id_cnum.get(), issuing_authority=id_authority.get())
    new_contact_info = ContactInformation(type=contact_type.get(), contact_information=contact_info.get())
    new_distributor = Distributors(name=name.get(), last_name=last_name.get(), date_of_birth=dob.get(), gender=gender.get(), image=image.get(), contact_information=new_contact_info, identity_information=new_id, address=new_address)
    data.data_saver.DataSaver.transfer_data_from_json("data/distributors.json")
    data.data_saver.DataSaver.to_runtime_data(new_distributor)
    data.data_saver.DataSaver.transfer_data_to_json(data.data_saver.DataSaver.runtime_data, "data/distributors.json")
    for key, value in data.data_saver.DataSaver.runtime_data.items():
       data.data_saver.DataSaver.runtime_data[key] = data.data_saver.DataSaver.create_distributor_from_runtime_data(key, value)


def browse_image(entry_field):
    file_path = filedialog.askopenfilename()
    entry_field.delete(0, END)
    entry_field.insert(0, file_path)


def new_distributor_page():
    root = Tk()
    root.title("New User Window")
    root.geometry("850x1000")

    # Labels
    title = Label(root, text="New User", font=("Arial", 36))
    name_title = Label(root, text="First Name:", font=("Arial", 16))
    last_name_title = Label(root, text="Last Name:", font=("Arial", 16))
    gender_title = Label(root, text="Gender:", font=("Arial", 16))
    image_title = Label(root, text="Image:", font=("Arial", 16))
    dob_title = Label(root, text="Date of Birth:", font=("Arial", 16))
    contact_type_title = Label(root, text="Contact Type:", font=("Arial", 16))
    contact_info_title = Label(root, text="Contact Information:", font=("Arial", 16))
    id_type_title = Label(root, text="ID Type:", font=("Arial", 16))
    id_issue_title = Label(root, text="ID Date of Issue:", font=("Arial", 16))
    id_expiry_title = Label(root, text="ID Date of Expiry:", font=("Arial", 16))
    id_pnum_title = Label(root, text="ID Personal Number:", font=("Arial", 16))
    id_series_title = Label(root, text="ID Series:", font=("Arial", 16))
    id_cnum_title = Label(root, text="ID Card Number:", font=("Arial", 16))
    id_authority_title = Label(root, text="ID Issuing Authority:", font=("Arial", 16))
    addr_type_title = Label(root, text="Address Type:", font=("Arial", 16))
    addr_title = Label(root, text="Address:", font=("Arial", 16))
    referrer_title = Label(root, text="Referrer:", font=("Arial", 16))

    # Entry Fields
    name_entry = Entry(root, width=50)
    last_name_entry = Entry(root, width=50)
    gender_entry = Entry(root, width=50)
    image_entry = Entry(root, width=50)
    dob_entry = Entry(root, width=50)
    contact_type_entry = Entry(root, width=50)
    contact_info_entry = Entry(root, width=50)
    id_type_entry = Entry(root, width=50)
    id_issue_entry = Entry(root, width=50)
    id_expiry_entry = Entry(root, width=50)
    id_pnum_entry = Entry(root, width=50)
    id_series_entry = Entry(root, width=50)
    id_cnum_entry = Entry(root, width=50)
    id_authority_entry = Entry(root, width=50)
    addr_type_entry = Entry(root, width=50)
    addr_entry = Entry(root, width=50)
    referrer_entry = Entry(root, width=50)

    # Buttons
    image_button = Button(root, text="Browse", command=lambda: browse_image(image_entry))
    save_button = Button(root, text="Save User", width=15, command=lambda: save_user(name_entry, last_name_entry, gender_entry, image_entry, dob_entry, contact_type_entry, contact_info_entry, id_type_entry, id_issue_entry, id_expiry_entry, id_pnum_entry, id_series_entry, id_cnum_entry, id_authority_entry, addr_type_entry, addr_entry))
    cancel_button = Button(root, text="Cancel", width=20, command=root.destroy)

    # Placing Widgets
    title.grid(row=0, column=0, padx=10, pady=20, columnspan=2, sticky="w")
    name_title.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
    name_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
    last_name_title.grid(row=3, column=0, padx=10, pady=10, sticky="nw")
    last_name_entry.grid(row=4, column=0, padx=10, pady=10, sticky="nw")
    gender_title.grid(row=5, column=0, padx=10, pady=10, sticky="nw")
    gender_entry.grid(row=6, column=0, padx=10, pady=10, sticky="nw")
    image_title.grid(row=7, column=0, padx=10, pady=10, sticky="nw")
    image_entry.grid(row=8, column=0, padx=10, pady=10, sticky="nw")
    image_button.grid(row=8, column=1, padx=10, pady=10, sticky="w")
    dob_title.grid(row=9, column=0, padx=10, pady=10, sticky="nw")
    dob_entry.grid(row=10, column=0, padx=10, pady=10, sticky="nw")
    contact_type_title.grid(row=11, column=0, padx=10, pady=10, sticky="nw")
    contact_type_entry.grid(row=12, column=0, padx=10, pady=10, sticky="nw")
    contact_info_title.grid(row=13, column=0, padx=10, pady=10, sticky="nw")
    contact_info_entry.grid(row=14, column=0, padx=10, pady=10, sticky="nw")
    id_type_title.grid(row=13, column=2, padx=10, pady=10, sticky="nw")
    id_type_entry.grid(row=14, column=2, padx=10, pady=10, sticky="nw")
    id_issue_title.grid(row=1, column=2, padx=10, pady=10, sticky="nw")
    id_issue_entry.grid(row=2, column=2, padx=10, pady=10, sticky="nw")
    id_expiry_title.grid(row=3, column=2, padx=10, pady=10, sticky="nw")
    id_expiry_entry.grid(row=4, column=2, padx=10, pady=10, sticky="nw")
    id_pnum_title.grid(row=5, column=2, padx=10, pady=10, sticky="nw")
    id_pnum_entry.grid(row=6, column=2, padx=10, pady=10, sticky="nw")
    id_series_title.grid(row=7, column=2, padx=10, pady=10, sticky="nw")
    id_series_entry.grid(row=8, column=2, padx=10, pady=10, sticky="nw")
    id_cnum_title.grid(row=9, column=2, padx=10, pady=10, sticky="nw")
    id_cnum_entry.grid(row=10, column=2, padx=10, pady=10, sticky="nw")
    id_authority_title.grid(row=11, column=2, padx=10, pady=10, sticky="nw")
    id_authority_entry.grid(row=12, column=2, padx=10, pady=10, sticky="nw")
    addr_type_title.grid(row=15, column=0, padx=10, pady=10, sticky="nw")
    addr_type_entry.grid(row=16, column=0, padx=10, pady=10, sticky="nw")
    addr_title.grid(row=17, column=0, padx=10, pady=10, sticky="nw")
    addr_entry.grid(row=18, column=0, padx=10, pady=10, sticky="nw")
    referrer_title.grid(row=15, column=2, padx=10, pady=10, sticky="nw")
    referrer_entry.grid(row=16, column=2, padx=10, pady=10, sticky="nw")
    save_button.grid(row=17, column=2, padx=10, pady=20, sticky="nw")
    cancel_button.grid(row=18, column=3, padx=10, pady=20, sticky="nw")

    root.grid_rowconfigure(index=0, weight=0)
    root.grid_rowconfigure(index=1, weight=0)
    root.grid_rowconfigure(index=35, weight=1)
    root.grid_columnconfigure(index=1, weight=0)
    root.grid_columnconfigure(index=0, weight=0)
    root.grid_columnconfigure(index=3, weight=1)

    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    new_distributor_page()
