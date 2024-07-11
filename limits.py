from helper import *
import os

def limits():
    file = os.path.join("expenses/expenses_limits.txt")
    print("Enter limits (Press enter to skip): ")
    try:
        weekly_limit = int(input("Enter weekly limit: ").strip())
    except ValueError:
        weekly_limit = reader(file)[0].split(" ")[2]
    try:
        monthly_limit = int(input("Enter monthly limit: ").strip())
    except ValueError:
        monthly_limit = reader(file)[1].split(" ")[2]
    with open(file, "w") as file:
        file.write(f"Weekly limit: {weekly_limit}\n")
        file.write(f"Monthly limit: {monthly_limit}\n")
    print("Changes applied successfully")

def check_exceed(month, year):
    choice = -1
    if input("Select (y) to check for week: ") == 'y':
        choice = 1
    else:
        choice = 0

    file = os.path.join("expenses/expenses_" + month + year + ".txt")
    data = reader(file)
    expense = 0
    for line in data:
        try:
            expense += int(line.split(",")[0])
        except:
            pass
    print(f"Expenditure in month till now: {expense}")

    file = os.path.join("expenses/expenses_limits.txt")
    data = reader(file)
    
    if choice:
        limit = int(data[0].split(" ")[2])
        print(f"Weekly Budget left: {limit + expense}")
        if expense >= limit:
            print("Weekly expense exceeded.")

    limit = int(data[1].split(" ")[2])
    print(f"Monthly Budget left: {limit + expense}")
    if expense >= limit:
        print("Monthly expense limit exceeded.")