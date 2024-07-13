import os

months = ['January', 'February', 'March', 'April', 
          'May', 'June', 'July', 'August', 
          'September', 'October', 'November', 'December']

def clear_screen():
    os.system('clear')

def reader(file):
    with open(file, "r") as file:
        data = file.read().split("\n")
    return data
