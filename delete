import os

path = "tes.txt"

try:
    os.remove(path)
except FileNotFoundError:
    print("That file is not found")
except PermissionError:
    print("You do not have a permission to delete that")
