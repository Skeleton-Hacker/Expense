expense_file = "expense.txt"

def options():
    print("Select option:")
    print("\t 1. Add entry")
    print("\t 2. Delete entry")
    print("\t 3. Filter")
    return input().strip()

def write_entry(entry):
    with open(expense_file, "a") as file:
        file.write(entry)

def add_entry():
    while(1):
        while(1):    
            type = input("Select Credit(+) or Debit(-): ").strip()
            if type == "+" or "-":
                break
        try:
            amount = int(input("Enter amount: "))
        except:
            pass
        date = input("Enter date(DD-MM-YY): ").strip()
        tag = input("Enter type of expense: ").strip()
        entry = type + amount + "," + date + "," + tag + "\n"
        print("Confirm entry(y) or skip(n):", entry )
        if input().strip() == 'y':
            write_entry(entry)
            break

add_entry()

