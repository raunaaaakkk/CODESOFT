import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                contacts_data = json.load(file)
                return [Contact(**data) for data in contacts_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return results

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        self.save_contacts()

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            print("\nContact List:")
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            if results:
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No contacts found.")

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            if contact_book.update_contact(name, new_contact):
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted successfully!")

        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()