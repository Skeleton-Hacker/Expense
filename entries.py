from datetime import datetime

expense_file = "expense.txt"

def write_entry(entry):
    with open(expense_file, "a") as file:
        file.write(entry)

def add_entry():
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
            date = input("Enter date(DD-MM-YY): ").strip()
            try:
                datetime.strptime(date, "%d-%m-%y")
                break
            except ValueError:
                print("Incorrect date format, use (DD-MM-YY)")

        tag = input("Enter type of expense: ").strip()
        entry = f"{type}{amount},{date},{tag}\n"
        confirmation = input(f"Confirm entry(y/n): {entry}")
        if confirmation == 'y':
            write_entry(entry)
            break


