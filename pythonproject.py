import os
import re

def log_action(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"\n Performing action: {action}")
            result = func(*args, **kwargs)
            print(f" Completed: {action}\n")
            return result
        return wrapper
    return decorator


def validate_contact(func):
    def wrapper(contact, *args, **kwargs):
        phone = contact.get("phone", "")
        email = contact.get("email", "")

        if not re.match(r"^[6-9]\d{9}$", phone):
            print("Invalid phone number! Must be 10 digits starting with 6–9.")
            return

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            print("Invalid email address!")
            return

        return func(contact, *args, **kwargs)
    return wrapper


FILE_NAME = "contacts.txt"


def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    name, phone, email, address = parts
                    contacts[phone] = {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "address": address
                    }
    return contacts


def save_contacts():
    with open(FILE_NAME, "w") as file:
        for c in contacts.values():
            file.write(f"{c['name']}|{c['phone']}|{c['email']}|{c['address']}\n")


@log_action("Add Contact")
@validate_contact
def add_contact(contact):
    if contact["phone"] in contacts:
        print("Contact with this phone number already exists!")
    else:
        contacts[contact["phone"]] = contact
        save_contacts()
        print("Contact added successfully!")


@log_action("Update Contact")
def update_contact():
    key = input("Enter name or phone to update: ")
    for phone, info in contacts.items():
        if key.lower() == info["name"].lower() or key == phone:
            print("Current Details:", info)
            new_name = input("Enter new name (press Enter to skip): ")
            new_phone = input("Enter new phone (press Enter to skip): ")
            new_email = input("Enter new email (press Enter to skip): ")
            new_address = input("Enter new address (press Enter to skip): ")

            if new_name:
                info["name"] = new_name
            if new_phone:
                info["phone"] = new_phone
            if new_email:
                info["email"] = new_email
            if new_address:
                info["address"] = new_address

            if new_phone and new_phone != phone:
                contacts.pop(phone)
                contacts[info["phone"]] = info

            save_contacts()
            print("Contact updated successfully!")
            return
    print("Contact not found!")


@log_action("Delete Contact")
def delete_contact():
    key = input("Enter name or phone to delete: ")
    for phone, info in list(contacts.items()):
        if key.lower() == info["name"].lower() or key == phone:
            del contacts[phone]
            save_contacts()
            print("Contact deleted successfully!")
            return
    print("Contact not found!")


@log_action("Search Contact")
def search_contact():
    key = input("Enter name or phone to search: ")
    for info in contacts.values():
        if key.lower() == info["name"].lower() or key == info["phone"]:
            print("\n--- Contact Found ---")
            print(f"Name: {info['name']}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            return
    print("No contact found!")


@log_action("Display All Contacts")
def show_all_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        print("\n--------- All Contacts ----------")
        for i, c in enumerate(contacts.values(), 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']} | {c['address']}")
        print("------------------------------")


contacts = load_contacts()

while True:
    print("\n------ Contact Book Menu ------")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Show All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1–6): ")

    match choice:
        case "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            add_contact(contact)

        case "2":
            update_contact()

        case "3":
            delete_contact()

        case "4":
            search_contact()

        case "5":
            show_all_contacts()

        case "6":
            print("Exit contact book")
            break

        case _:
            print("Invalid choice.")
