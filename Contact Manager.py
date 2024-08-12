import os
import csv

CONTACTS_FILE = 'contacts.txt'
EXPORT_CSV_FILE = 'contacts_export.csv'

def ensure_file_exists():
    """Ensure the contacts file exists."""
    if not os.path.exists(CONTACTS_FILE):
        open(CONTACTS_FILE, 'w').close()  # Create an empty file if it does not exist

def load_contacts():
    """Load contacts from the file."""
    ensure_file_exists()
    with open(CONTACTS_FILE, 'r') as file:
        contacts = file.readlines()
    return [contact.strip().split(',', 1) for contact in contacts]

def save_contacts(contacts):
    """Save contacts to the file."""
    ensure_file_exists()
    with open(CONTACTS_FILE, 'w') as file:
        for name, phone in contacts:
            file.write(f"{name},{phone}\n")

def add_contact(name, phone):
    """Add a new contact."""
    contacts = load_contacts()
    contacts.append((name, phone))
    save_contacts(contacts)
    print(f"Contact added: {name} - {phone}")

def view_contacts():
    """View all contacts."""
    contacts = load_contacts()
    if contacts:
        print("Contacts List:")
        for idx, (name, phone) in enumerate(contacts, start=1):
            print(f"{idx}. {name} - {phone}")
    else:
        print("No contacts found.")

def delete_contact(contact_number):
    """Delete a contact by its number."""
    contacts = load_contacts()
    if 0 < contact_number <= len(contacts):
        removed_contact = contacts.pop(contact_number - 1)
        save_contacts(contacts)
        print(f"Contact removed: {removed_contact[0]} - {removed_contact[1]}")
    else:
        print("Invalid contact number.")

def edit_contact(contact_number):
    """Edit a contact's details."""
    contacts = load_contacts()
    if 0 < contact_number <= len(contacts):
        name, phone = contacts[contact_number - 1]
        print(f"Editing contact: {name} - {phone}")
        new_name = input("Enter new name (leave blank to keep unchanged): ")
        new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
        if new_name:
            name = new_name
        if new_phone:
            phone = new_phone
        contacts[contact_number - 1] = (name, phone)
        save_contacts(contacts)
        print(f"Contact updated: {name} - {phone}")
    else:
        print("Invalid contact number.")

def export_contacts_to_csv():
    """Export contacts to a CSV file."""
    contacts = load_contacts()
    with open(EXPORT_CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone'])
        writer.writerows(contacts)
    print(f"Contacts exported to {EXPORT_CSV_FILE}")

def main():
    """Main function to run the contact manager."""
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Edit Contact")
        print("5. Export Contacts to CSV")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter the contact name: ")
            phone = input("Enter the contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            view_contacts()
            try:
                contact_number = int(input("Enter the contact number to delete: "))
                delete_contact(contact_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            view_contacts()
            try:
                contact_number = int(input("Enter the contact number to edit: "))
                edit_contact(contact_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            export_contacts_to_csv()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
