from tkinter import *
import data.data_saver
from Front_end.home_page import home_page
from Front_end.new_distributor_page import new_distributor_page

def show_identity_information(id_info):
    root = Tk()
    root.title("ID information")
    root.geometry("300x300")

    id_info_label = Label(root, text="ID Information", font=("Arial", 32))
    type_label = Label(root, text=f"Type: {id_info.type}", font=("Arial", 16))
    date_of_issue_label = Label(root, text=f"Date of Issue: {id_info.date_of_issue}", font=("Arial", 16))
    date_of_expiry_label = Label(root, text=f"Date of Expiry: {id_info.date_of_expiry}", font=("Arial", 16))
    personal_number = Label(root, text=f"Personal number: {id_info.personal_number}", font=("Arial", 16))
    serie_label = Label(root, text=f"Serie: {id_info.serie}", font=("Arial", 16))
    card_number = Label(root, text=f"Card Number: {id_info.card_number}", font=("Arial", 16))
    issuing_authority = Label(root, text=f"Issuing Authority: {id_info.issuing_authority}", font=("Arial", 16))

    id_info_label.pack()
    type_label.pack()
    date_of_issue_label.pack()
    date_of_expiry_label.pack()
    personal_number.pack()
    serie_label.pack()
    card_number.pack()
    issuing_authority.pack()

    root.resizable(False, False)
    root.mainloop()


def refresh_canvas(distributors_data, distributors_frame, canvas):
    print(distributors_data)
    for widget in distributors_frame.winfo_children():
        widget.destroy()

    for key, value in data.data_saver.DataSaver.runtime_data.items():
        data.data_saver.DataSaver.runtime_data[key] = data.data_saver.DataSaver.create_distributor_from_runtime_data(key, data.data_saver.DataSaver.runtime_data)
    distributors_data = data.data_saver.DataSaver.runtime_data
    print(distributors_data)

    i = 0
    for code, distributor_ in distributors_data.items():
        # image_path=distributor_.image
        # image = Image.open(image_path)
        # resized_image = image.resize((110, 120))
        # distributor_image = ImageTk.PhotoImage(resized_image)
        # images.append(distributor_image)

        # image_widget = Label(distributor_frame, image=distributor_image)
        # image_widget.image = distributor_image
        name = Label(distributors_frame, text=f"Name: {distributor_.name}", padx=1, anchor="w", font=("Arial", 12))
        last_name = Label(distributors_frame, text=f"Last Name: {distributor_.last_name}", padx=1, anchor="w", font=("Arial", 12))
        gender = Label(distributors_frame, text=f"Gender: {distributor_.gender}", padx=1, anchor="s", font=("Arial", 12))
        date_of_birth = Label(distributors_frame, text=f"Date of Birth: {distributor_.date_of_birth}", padx=1, anchor="n", font=("Arial", 12))
        contact_information = Label(distributors_frame, text=f"Contact information: {str(distributor_.contact_information)}", padx=1, anchor="n", font=("Arial", 12))
        address = Label(distributors_frame, text=f"Address: {distributor_.address}", padx=1, anchor="n", font=("Arial", 12))
        referrer = Label(distributors_frame, text=f"Referrer: {distributor_.referrer}", padx=1, anchor="e", font=("Arial", 12))
        referral = Label(distributors_frame, text=f"Referral: {distributor_.referral}", padx=1, anchor="n", font=("Arial", 12))

        identity_information = Button(distributors_frame, text="Detailed ID information", padx=1, command=lambda d=distributor_: show_identity_information(d.identity_information))

        name.grid(row=i, column=1, padx=(10, 50), pady=3, sticky="nw")
        last_name.grid(row=i + 1, column=1, padx=(10, 50), pady=3, sticky="w")
        gender.grid(row=i + 2, column=1, padx=(10, 50), pady=3, sticky="sw")
        # image_widget.grid(row=i, column=0, padx=10, pady=5, sticky="nswe", rowspan=3)
        date_of_birth.grid(row=i, column=2, padx=10, pady=5, sticky="nw")
        contact_information.grid(row=i + 1, column=2, padx=10, pady=5, sticky="w")
        address.grid(row=i + 2, column=2, padx=10, pady=5, sticky="sw")
        referrer.grid(row=i + 1, column=3, padx=10, pady=5, sticky="w")
        referral.grid(row=i + 2, column=3, padx=10, pady=5, sticky="sw")
        identity_information.grid(row=i, column=3, padx=10, pady=5, sticky="e")

        i += 3

    # Update the scroll region of the canvas
    distributors_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


def distributors_page(distributors):
    distributors_data = distributors

    root = Tk()
    root.title("Distributos Page")
    root.geometry("1100x700")

    distributor_list_frame = LabelFrame(root, padx=5, pady=5)
    canvas = Canvas(distributor_list_frame)
    scrollbar = Scrollbar(distributor_list_frame, orient=VERTICAL, command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)


    # Create a frame inside the canvas
    distributor_frame = Frame(canvas)
    canvas.create_window((0, 0), window=distributor_frame, anchor='center')

    images = []


    i = 0
    for code, distributor_ in distributors_data.items():
        # image_path=distributor_.image
        # image = Image.open(image_path)
        # resized_image = image.resize((110, 120))
        # distributor_image = ImageTk.PhotoImage(resized_image)
        # images.append(distributor_image)

        # image_widget = Label(distributor_frame, image=distributor_image)
        # image_widget.image = distributor_image
        name = Label(distributor_frame, text=f"Name: {distributor_.name}", padx=1, anchor="w", font=("Arial", 12))
        last_name = Label(distributor_frame, text=f"Last Name: {distributor_.last_name}", padx=1, anchor="w", font=("Arial", 12))
        gender = Label(distributor_frame, text=f"Gender: {distributor_.gender}", padx=1, anchor="s", font=("Arial", 12))
        date_of_birth = Label(distributor_frame, text=f"Date of Birth: {distributor_.date_of_birth}", padx=1, anchor="n", font=("Arial", 12))
        contact_information = Label(distributor_frame, text=f"Contact information: {str(distributor_.contact_information)}", padx=1, anchor="n", font=("Arial", 12))
        address = Label(distributor_frame, text=f"Address: {distributor_.address}", padx=1, anchor="n", font=("Arial", 12))
        referrer = Label(distributor_frame, text=f"Referrer: {distributor_.referrer}", padx=1, anchor="e", font=("Arial", 12))
        referral = Label(distributor_frame, text=f"Referral: {distributor_.referral}", padx=1, anchor="n", font=("Arial", 12))

        identity_information = Button(distributor_frame, text="Detailed ID information", padx=1, command=lambda d=distributor_: show_identity_information(d.identity_information))


        name.grid(row=i, column=1, padx=(10, 50), pady=3, sticky="nw")
        last_name.grid(row=i+1, column=1, padx=(10, 50), pady=3, sticky="w")
        gender.grid(row=i+2, column=1, padx=(10, 50), pady=3, sticky="sw")
        # image_widget.grid(row=i, column=0, padx=10, pady=5, sticky="nswe", rowspan=3)
        date_of_birth.grid(row=i, column=2, padx=10, pady=5, sticky="nw")
        contact_information.grid(row=i+1, column=2, padx=10, pady=5, sticky="w")
        address.grid(row=i+2, column=2, padx=10, pady=5, sticky="sw")
        referrer.grid(row=i+1, column=3, padx=10, pady=5, sticky="w")
        referral.grid(row=i+2, column=3, padx=10, pady=5, sticky="sw")
        identity_information.grid(row=i, column=3, padx=10, pady=5, sticky="e")

        i += 3



    # Update the scroll region of the canvas
    distributor_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))


    # Labels
    distributor_label = Label(root, text="Distributors", bd=1, font=("Arial", 32), padx=1, anchor='w')


    # Buttons
    back_to_home_page = Button(root, text="<--- Home page", width=20, pady=10, command=lambda: home_page(data.data_saver.DataSaver.runtime_data, data.data_saver.DataSaver.products_runtime_data, data.data_saver.DataSaver.sales_runtime_data))
    add_distributor_button = Button(root, text="New Distributor!", width=20, padx=40, pady=10, command=new_distributor_page)
    refresh_list_button = Button(root, text="Refresh List!", width=20, padx=40, pady=10, command=lambda:refresh_canvas(distributors_data=data.data_saver.DataSaver.runtime_data, distributors_frame=distributor_frame, canvas=canvas))

    # Grid configuration
    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=0)
    root.grid_rowconfigure(index=0, weight=0)
    root.grid_rowconfigure(index=1, weight=0)
    root.grid_rowconfigure(index=2, weight=1)
    distributor_list_frame.grid_rowconfigure(index=0, weight=1)
    distributor_list_frame.grid_columnconfigure(index=0, weight=1)

    # Putting stuff on screen
    back_to_home_page.grid(row=0, column=0, padx=5, pady=10)
    add_distributor_button.grid(row=1, column=2, padx=10, pady=10)
    refresh_list_button.grid(row=1, column=3, padx=10, pady=10)
    distributor_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="w")
    distributor_list_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=4, sticky="nwes")
    canvas.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")


    root.mainloop()

if __name__ == "__main__":
    distributors_page()
