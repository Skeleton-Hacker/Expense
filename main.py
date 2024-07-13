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
            print("Select the month and year to the specified")
            month = input("Month: ")
            year = input("Year: ")
            clear_screen()
            choice = options()
            clear_screen()
            if choice == 1:
                add_entry(month, year)
            elif choice == 5:     
                limits()
            choice = input("Continue(y/n): ")
            if choice.lower() == 'n':
                clear_screen()
                print("All changes have been saved successfully")
                check_exceed(month, year)
                break
        except KeyboardInterrupt:
            clear_screen()
            print("All changes have been saved successfully")
            try:
                choice = input("Continue(y/n): ")
                if choice.lower() == 'y':
                    continue
                check_exceed(month, year)
            except:
                print("Month and Year not provided. Aborting.")
            break
        except:
            print("Error encountered, try again")

if __name__ == "__main__":
    main()