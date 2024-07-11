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