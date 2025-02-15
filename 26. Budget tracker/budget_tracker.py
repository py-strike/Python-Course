import json

def view_budget(data):
    print("view_budget")
    return data

def add_budget(data):
    name = input("Enter the name of the new category : ")
    amount = int(input("Enter the budget amount : "))
    new_item = {
        'name': name,
        'amount': amount,
    }
    data['categories'].append(new_item)

    return data

def remove_budget(data):
    name = input("Enter the name of the category you want to remove : ")
    data['categories'] = [c for c in data['categories'] if c['name'] != name]
    return data

def add_expense(data):
    name = input("Enter the name of the new Expense : ")
    amount = int(input("Enter the budget amount : "))
    new_item = {
        'name': name,
        'amount': amount,
    }
    data['expenses'].append(new_item)
    return data

def remove_expense(data):
    name = input("Enter the name of the expense you want to remove : ")
    data['expenses'] = [c for c in data['expenses'] if c['name'] != name]
    return data

def exit_program(data):
    print("exit_program")
    return data

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
        updated_data = chosen_action['action'](Budget_tracker_data)

        print("----------------------")

        with open(file_name, "w") as file:
            json.dump(updated_data, file)

run_program(possible_actions, 'budget_tracker_data.json')


