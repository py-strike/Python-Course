possible_actions = [
    {'name': 'View Budget'},
    {'name': 'Add Budget'},
    {'name': 'Remove Budget'},
    {'name': 'Add Expense'},
    {'name': 'Remove Expense'},
    {'name': 'Exit Program'},
]

def run_program(actions):
    while True:
        print("Choose an action : ")
        for index, action in enumerate(actions):
            print(f"{index + 1}. {action['name']}.")
        
        user_chosse = input("--> ")
        chosen_action = possible_actions[int(user_chosse) - 1]['name']
        print(f"Y'ouve chosen : {chosen_action}")
        print("----------------------")

run_program(possible_actions)

# init_msg = ""

# while True:
#     responce = input(init_msg)
#     print("----------------------")
#     if responce == "1":
#         view_budget(shopping_list)
#         print("----------------------")
#     elif responce == "2":
#         add_remove_items(shopping_list)
#         print("----------------------")
#     elif responce == "3":
#         add_remove_items(shopping_list)
#         print("----------------------")
#     elif responce == "4":
#         print("Quiting")
#         print("----------------------")
#         break
#     else:
#         print("this is not a valid option")

#     with open("shopping_list.json", "w") as file:
#         json.dump(shopping_list, file)
