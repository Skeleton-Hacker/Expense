import os

def clear_screen():
    os.system('clear')

def reader(file):
    with open(file, "r") as file:
        data = file.read().split("\n")
    return data
