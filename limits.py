from helper import *
import os

def limits():
    file = os.path.join("expenses/expenses_limits.txt")
    print("Enter limits (Press enter to skip): ")
    try:
        monthly_limit = int(input("Enter monthly limit: ").strip())
    except ValueError:
        monthly_limit = reader(file)[1].split(" ")[2]
    with open(file, "w") as file:
        file.write(f"Monthly limit: {monthly_limit}\n")
    print("Changes applied successfully")

def check_exceed(month, year):
    try:
        file = os.path.join("expenses/expenses_" + month + year + ".txt")
        data = reader(file)
    except:
        print("The given data does not exist.")
        return 
    expense = 0
    for line in data:
        try:
            expense += int(line.split(",")[0])
        except:
            pass
    print(f"Expenditure in month till now: {expense}")

    file = os.path.join("expenses/expenses_limits.txt")
    data = reader(file)

    limit = int(data[1].split(" ")[2])
    print(f"Monthly Budget left: {limit + expense}")
    if expense >= limit:
        print("Monthly expense limit exceeded.")