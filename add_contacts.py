from save_contacts import save_contact

def add_contact():
    try:
        name = input("Enter Contact Name: ")
        email = input("Enter Contact Email: ")
        phone_no = int(input("Enter Contact Phone No: "))
        nid_no = int(input("Enter Contact NID No.: "))
        address = input("Enter Contact Address: ")

        save_contact(name, email, phone_no, nid_no, address)

    except Exception  as e:
        raise Exception(f"Error message....{e}")

