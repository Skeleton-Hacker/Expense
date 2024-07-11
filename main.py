from entries import *
from limits import *
from helper import *

def options():
    print("Select option:")
    print("\t 1. Add entry")
    print("\t 2. Current Month Expense")
    print("\t 3. Monthly expense overview")
    print("\t 4. Filter")
    print("\t 5. Set Expense limits")
    return int(input().strip())

def main():
    choice = options()
    clear_screen()
    month = input("Month: ")
    year = input("Year: ")
    if choice == 1:
        add_entry(month, year)
    elif choice == 2:
        print("Select option:")
        print("\t a. Month")
        print("\t b. Variance over Months")
        print("\t c. ")
    elif choice == 5:     
        limits()
    
    check_exceed(month, year)

if __name__ == "__main__":
    main()