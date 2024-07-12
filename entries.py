import os
from helper import *

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
            date = int(input("Enter date: ").strip())
            if date not in range(31):
                print("Incorrect date")
            else:
                break

        tag = input("Enter type of expense: ").strip()
        entry = f"{type}{amount},{date} {month} {year},{tag}\n"
        file = os.path.join("expenses/expenses_" + month + year + ".txt")
        write_entry(entry, file)
        file = os.path.join("expenses/Variables.txt")
        data = reader(file)
        balance = int(data[0].split(" ")[2])
        balance += int(f"{type}{amount}")
        monthly_limit = reader(file)[1].split(" ")[2]
        with open(file, 'w') as file:
            file.write(f"Current balance: {balance}\n")
            file.write(f"Monthly limit: {monthly_limit}\n")
        choice = input("Add another entry(y/n): ")
        if choice.lower() == "y":
            clear_screen()
            continue
        else:
            break


