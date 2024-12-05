import csv
def delete_by_row(row):
    with open('all_contacts.csv', 'r') as file:
        reader = csv.reader(file)
        contacts = list(reader)
        if row < 1 or row > len(contacts):
            print(f"Invalid row number: {row}. File has {len(contacts)} rows.")
            return

        removed_row = contacts.pop(row - 1)  # Subtract 1 because row_number is 1-based
        print(f"Deleted row: {row}")

        with open('all_contacts.csv', mode='w', newline='') as file2:
            writer = csv.writer(file2)
            writer.writerows(contacts)

        print(f"Row {row} deleted successfully.")


