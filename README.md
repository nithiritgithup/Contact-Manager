Contact Manager Program with CSV Export
This Python program serves as a simple contact manager that allows users to manage their contact list with features for adding, viewing, editing, and deleting contacts. Additionally, it includes functionality to export contacts to a CSV file for easy data handling and sharing. Below is an overview of the program's features:

Features:
Add Contact

Functionality: Users can add a new contact by providing a name and a phone number.
Implementation: The contact is appended to the list and saved to a text file (contacts.txt).
View Contacts

Functionality: Displays a list of all contacts with their names and phone numbers.
Implementation: Contacts are read from the text file and printed to the console. If no contacts are available, a relevant message is shown.
Delete Contact

Functionality: Allows users to delete a contact by specifying its number in the list.
Implementation: The contact is removed from the list, and the updated list is saved back to the text file.
Edit Contact

Functionality: Users can update the details of an existing contact. They can modify the name, phone number, or both.
Implementation: After selecting the contact to edit, users are prompted to enter new details. If provided, these details update the contact's information in the list.
Export Contacts to CSV

Functionality: Exports the contact list to a CSV file for easier management and sharing.
Implementation: Contacts are written to a file named contacts_export.csv in CSV format. The file includes headers ("Name" and "Phone") and the contact details.
File Management

Functionality: Ensures the contact file exists before performing read or write operations.
Implementation: A helper function creates an empty contacts.txt file if it does not already exist.
How It Works:
Initialization: The program begins by checking if the contact file exists. If not, it creates an empty file.
Main Menu: A loop provides a menu with options to add, view, edit, delete contacts, export contacts to CSV, or exit the program.
User Input: Based on user choices, the program invokes the appropriate functions to manage contacts.
File Handling: Contacts are managed in a text file for persistent storage and can be exported to a CSV file for better usability.
