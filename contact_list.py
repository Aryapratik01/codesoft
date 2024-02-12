# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:12:09 2024

@author: aryap
"""

contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def search_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def update_contact(name, new_phone="", new_email=""):
    if name in contacts:
        if new_phone:
            contacts[name]["phone"] = new_phone
        if new_email:
            contacts[name]["email"] = new_email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def view_contacts():
    if contacts:
        for name, contact in contacts.items():
            print(f"{name}: {contact['phone']}, {contact['email']}")
    else:
        print("Contact list is empty.")

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. View contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email (optional): ")
        add_contact(name, phone, email)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "4":
        name = input("Enter name to update: ")
        new_phone = input("Enter new phone number (optional): ")
        new_email = input("Enter new email (optional): ")
        update_contact(name, new_phone, new_email)
    elif choice == "5":
        view_contacts()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
