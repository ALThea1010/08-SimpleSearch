"""
Assessment1-Programming-Skills-Portfolio Exercise 8: Simple Search
"""

list_of_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  # list of names

name = input("Enter the name you want to search in the list --> ")

# Check if the name exists in the list before using .index()
if name in list_of_names:
    print("The position of", name, "in the list is:", list_of_names.index(name))
else:
    print(name, "is not found in the list.")
