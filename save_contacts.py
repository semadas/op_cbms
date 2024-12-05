import csv
def save_contact(name, email, phone_no, nid_no, address):
    with open("all_contacts.csv", mode="r") as myFile:
        reader = csv.reader(myFile)
        contacts = list(reader)

        for contact in contacts:
            if len(contact) > 0 and int(contact[2]) == phone_no:
                print(contact[2])
                print(f"Phone: {phone_no} already exists.")
                return
    with open("all_contacts.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone_no, nid_no, address])
    print("Record added successfully.")





