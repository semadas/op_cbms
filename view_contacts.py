import csv
def view_all_contacts(all_contacts):
    #if all_contacts != []:
    with open("all_contacts.csv", mode="r") as myFile:

        reader = csv.reader(myFile)
        contacts = list(reader)
        for contact in contacts:
            print(f"{contact}\n")



