from datetime import datetime

expense_file = "expense.txt"

def write_entry(entry):
    with open(expense_file, "a") as file:
        file.write(entry)

def add_entry():
    while(1):
        while(1):    
            type = input("Select Credit(+) or Debit(-): ").strip()
            if type == "+" or "-":
                break
            else:
                print("Invalid response,", end = " ")

        while(1):
            try:
                amount = int(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid amount")

        while(1):    
            date = input("Enter date(DD-MM-YY): ").strip()
            try:
                datetime.strptime(date, "%d-%m-%y")
                break
            except ValueError:
                print("Incorrect date format, use (DD-MM-YY)")

        tag = input("Enter type of expense: ").strip()
        entry = type + amount + "," + date + "," + tag + "\n"
        print("Confirm entry(y) or skip(n):", entry, end = "")
        if input().strip() == 'y':
            write_entry(entry)
            break


