import os

def write_entry(entry, file):
    with open(file, "a") as file:
        file.write(entry)

def add_entry(month, year):
    while True:
        while True:    
            type = input("Select Credit(+) or Debit(-): ").strip()
            if type in ("+", "-"):
                break
            else:
                print("Invalid response,", end = " ")

        while True:
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid amount")

        while True:    
            date = int(input("Enter date(DD): ").strip())
            if date not in range(31):
                print("Incorrect date")
            else:
                break

        tag = input("Enter type of expense: ").strip()
        entry = f"{type}{amount},{date} {month} {year},{tag}\n"
        file = os.path.join("expenses/" + "expense_" + month + year + ".txt")
        write_entry(entry, file)
        choice = input("Add another entry(y/n): ")
        if choice == "y":
            continue
        else:
            break


