from add_contacts import add_contact
import add_contacts
import view_contacts
import delete_contacts

all_contacts =[]

while True:
    print("Welcome to Contact Management System")
    print("0: Exit")
    print("1. Add Contacts")
    print("2. View all Contacts")
    print("3. Delete Contacts by Row no.")

    option = input("Please choose your option: ")

    if option == "0":
        print("Thank for using Contact Management System")
        break
    elif option == "1":
        all_contacts = add_contacts.add_contact()
    elif option == "2":
        view_contacts.view_all_contacts(all_contacts)
    elif option == "3":
        row = int(input("Enter row no. to delete: "))
        delete_contacts.delete_by_row(row)

    else:
        print("Enter a valid option")





