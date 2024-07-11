from entries import *

def options():
    print("Select option:")
    print("\t 1. Add entry")
    print("\t 2. Delete entry")
    print("\t 3. Filter")
    return int(input().strip())

def main():
    choice = options()
    if choice == 1:
        add_entry()

if __name__ == "__main__":
    main()