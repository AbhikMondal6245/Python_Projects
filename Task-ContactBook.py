def main():  # defines the function named main
    contact_book = ContactBook()  # creates an instance of the ContactBook class and assigned to contact_book variable

    # after completing the operation, for asking the user to continue with another operation,
    # and take input from user and then as per choice recall the function again using while loop.
    while True:
        print("_____Contact Book_____")
        print("[        MENU        ]")
        print("1. Add Contact")
        print("2. Display Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit Contact Book")

        user_choice = input("Enter your choice : ")  # for taking the input from user to continue with selected choice

        if user_choice == "1":
            name = input("Enter Contact name : ")
            phone_number = input("Enter phone number : ")
            email = input("Enter email address : ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
            print(name, "has been added to your contacts.")

        elif user_choice == "2":
            contact_book.display_contacts()

        elif user_choice == "3":
            search_char = input("Enter name or phone number to search: ")
            matching_contacts = contact_book.search_contact(search_char)
            if matching_contacts:
                print("Matching Contacts are : ")
                # iterate through a sequence of objects stored in the matching_contacts variable
                # while keeping track of the index of each item
                for i, contact in enumerate(matching_contacts, start=1):
                    print(f"{i}. {contact.name} - {contact.phone_number}")
            else:
                print("[ No matching contacts found. ]")

        elif user_choice == "4":
            # here index means the positions or ranking of contacts
            # asking user which contact they want to update and take input from user
            index = int(input("Enter the index(Position) of the contact to update: "))
            if 0 < index <= len(contact_book.contacts):
                name = input("Enter the updated name : ")
                phone_number = input("Enter the updated phone number : ")
                email = input("Enter the updated email : ")
                address = input("Enter the updated address : ")
                updated_contact = Contact(name, phone_number, email, address)
                contact_book.update_contact(index, updated_contact)
            else:
                print("[ Invalid contact index(Position). ]")

        elif user_choice == "5":
            # asking user which contact they want to delete and take input from user
            index = int(input("Enter the index of the contact to delete: "))
            contact_book.delete_contact(index)

        elif user_choice == "6":
            print("_______________________")
            print("Exiting Contact Book...")
            break

        else:
            print("[ Invalid choice, Please select again. ]")


class Contact:
    # Contact class is called for creating a new instance of the class.
    # It takes the parameters which are used to initialize the attributes of the class.
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        # assigns the parameters passed to the constructor to the attributes of the class Contact instance


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self, search_term):
        matching_contacts = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                matching_contacts.append(contact)
        return matching_contacts

    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("[ Invalid contact index ]")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(deleted_contact.name, "has been deleted.")
        else:
            print("[ Invalid contact index. ]")


if __name__ == "__main__":  # allows the program to be executable by itself
    main()
