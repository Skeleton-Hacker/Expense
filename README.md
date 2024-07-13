# CLI Expense Tracker

A terminal-based program to manage personal expenses easily. Features include:
- Adding expenses
- Setting monthly expense limit
- Ability to monitor the current balance after transactions

## How to use
First install all the requirements by
```
pip install -r requirements.txt
``` 

Then run:
```
python3 main.py
```
To exit the program, press `Ctrl+C`. This will save all changes to the required files, and provide a brief overview of the current balance as well as the month's expenditure. 

## Brief overview of Functions
### Add entry:
- Adds the specified amount to the current balance.
- Adds the details of the expense to the file of the specified month

The expenses of the specified month will be stored in the folder `expenses` with the name `expenses_(month)(year).txt`. Each entry will be saved as `amount,date, tag`. The tag is used to describe the type of expense. To assign multiple tags, separate by a comma. 

### Set Expense Limits
- Allows to edit the current balance
- Set the monthly expenditure limit

## Points to remember
1. At the start of the program
	- Enter the name of the entire month (for example: August, not Aug or any other variation)
	- Enter the year in 20xx format (for example: 2024)
This will be used for the entirety of the next operation. To change the month/year, enter `y` when continue is asked. 
2. If any error is made while inputing the data, press `Ctrl+C` 
3. In all cases, '+' denotes money saved, '-' denotes money spent