from entries import *
from limits import *
from helper import *

def options():
    print("Select option:")
    print("\t 1. Add entry")
    # print("\t 2. Current Month Expense")
    # print("\t 3. Monthly expense overview")
    # print("\t 4. Filter")
    print("\t 5. Set Expense limits")
    print("To exit, press 'Ctrl + C'")
    return int(input().strip())

def main():
    while True:
        try:
            clear_screen()
            month = input("Month: ")
            year = input("Year: ")
            clear_screen()
            choice = options()
            clear_screen()
            if choice == 1:
                add_entry(month, year)
            elif choice == 5:     
                limits()
        except KeyboardInterrupt:
            clear_screen()
            print("All changes have been saved successfully")
            check_exceed(month, year)
            break
        except:
            print("Invalid command, try again")

if __name__ == "__main__":
    main()