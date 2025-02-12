import json
import os

init_msg = "What you want to Do?\n" \
"1. View List.\n" \
"2. Add to the List.\n" \
"3. Remove from the List.\n" \
"4. Quit.\n" \
"Your choice is : "

# Check if the file exists, if not create it with an empty list
if not os.path.exists("shopping_list.json"):
    with open("shopping_list.json", "w") as file:
        json.dump([], file)

with open('shopping_list.json', 'r') as file:
    shopping_list = json.load(file)

def view_list(shopping_list: list):
    for index, item in enumerate(shopping_list):
        print(f"{index + 1}. {item['name']} | {item['quantity']}")

def add_to_list(shopping_list: list):
    name = input("Product name : ")
    quantity = input("Product quantity : ")

    new_product = {
        "name": name,
        "quantity": quantity
    }

    shopping_list.append(new_product)
    print(f"Product {name} added.")

def remove_from_list(shopping_list: list):
    view_list(shopping_list)
    print()

    number_to_remove_str = input("Enter the number of the item you want to remove : ")

    try:
        number_to_remove = int(number_to_remove_str)
    except ValueError:
        print("That is not a valid number.")
    else:
        if number_to_remove >= len(shopping_list):
            print("That number is not in the list")
        else:
            del shopping_list[number_to_remove - 1]
            print(f"The Item number {number_to_remove} was deleted")
    

while True:
    responce = input(init_msg)
    print("----------------------")
    if responce == "1":
        view_list(shopping_list)
        print("----------------------")
    elif responce == "2":
        add_to_list(shopping_list)
        print("----------------------")
    elif responce == "3":
        remove_from_list(shopping_list)
        print("----------------------")
    elif responce == "4":
        print("Quiting")
        print("----------------------")
        break
    else:
        print("this is not a valid option")

    with open("shopping_list.json", "w") as file:
        json.dump(shopping_list, file)

