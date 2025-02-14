import json

def view_budget():
    print("view_budget")

def add_budget():
    print("add_budget")

def remove_budget():
    print("remove_budget")

def add_expense():
    print("add_expense")

def remove_expense():
    print("remove_expense")

def exit_program():
    print("exit_program")

possible_actions = [
    {'name': 'View Budget',
     'action': view_budget},
    {'name': 'Add Budget',
     'action': add_budget},
    {'name': 'Remove Budget',
     'action': remove_budget},
    {'name': 'Add Expense',
     'action': add_expense},
    {'name': 'Remove Expense',
     'action': remove_expense},
    {'name': 'Exit Program',
     'action': exit_program},
]

def run_program(actions, file_name):
    while True:
        with open(file_name, 'r') as file:
            Budget_tracker_data = json.load(file)
        
        print("Choose an action : ")
        for index, action in enumerate(actions):
            print(f"{index + 1}. {action['name']}.")
        
        user_chosse = input("--> ")
        chosen_action = possible_actions[int(user_chosse) - 1]
        updated_data = chosen_action['action']()
        print("----------------------")

        with open(file_name, "w") as file:
            json.dump(updated_data, file)

run_program(possible_actions, 'budget_tracker_data.json')


