import os
from helper import *

def overview(month, year):
    try:
        file = os.path.join("expenses/expenses_" + month + year + ".txt")
        data = reader(file)
    except:
        print("The given data does not exist.")

    index = 0
    while index < 12:
        if months[index] == month:
            break
        index += 1
    if index == 0:
        year -= 1
    
    data_prev = 0
    try:
        file_prev = os.path.join("expenses/expenses_" + months[index] + year + ".txt")
        data_prev = reader(file_prev)
    except:
        pass

    return data, data_prev

def amount_categorize(data, data_prev):
    amount_added = 0
    amount_deducted = 0
    for line in data:
        amt = int(line.split(",")[0])
        if amt > 0:
            amount_added += amt
        else:
            amount_deducted += amt
    print(f"Amount added: {amount_added}")
    print(f"Amount spent: {amount_deducted}")

    amount_added_prev = 0
    amount_deducted_prev = 0
    if data_prev != 0:
        for line in data_prev:
            amt = int(line.split(",")[0])
            if amt > 0:
                amount_added_prev += amt
            else:
                amount_deducted_prev += amt
        print("Change from previous month:")
        print(f"\tAmount added: {amount_added - amount_added_prev}")
        print(f"\t Amount deducted: {amount_deducted - amount_deducted_prev}")
    
    file = os.path.join("expenses/Variables.txt")
    monthly_limit = reader(file)[1].split(" ")[2]
    monthly_save = monthly_limit + amount_added - amount_deducted
    print(f"Amount left in month's budget: {monthly_save}")
    return monthly_save

def spending_overview(data, month, year, monthly_save):
    expenditure = []
    for line in data:
        amt_info = line.split(",")[0]
        type_info = line.split(",")[2]
        for item in expenditure:
            if type_info == item[0]:
                item[1] += amt_info
            else:
                new_item = [type_info, amt_info]
                expenditure.append(new_item)
    expenditure.sort(key = lambda x: x[1])
    file = os.path.join("overview/" + month + year + ".txt")
    with open(file, 'w') as file:
        file.write(monthly_save)
        for line in expenditure:
            print(f"{line[0]}: line[1]")
            file.write(f"line[0]: line[1]\n")
    



