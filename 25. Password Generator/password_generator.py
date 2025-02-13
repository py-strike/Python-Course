import random

def password_generator(lenght: int, charset: list, other_options):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_uppercase = letters.upper()
    numbers = '012345689'
    symbols = '!@#$%()+-='

    new_password = []
    number_of_each = lenght // 4
    remaining_count = lenght % 4

    nb_of_lower = number_of_each + remaining_count
    nb_of_upper = number_of_each
    nb_of_characters = number_of_each
    nb_of_numbers = number_of_each

    for _ in range(nb_of_lower):
        new_letter = letters[random.randint(0, len(letters) - 1)]
        new_password.append(new_letter)
    
    for _ in range(nb_of_upper):
        new_letter = letters_uppercase[random.randint(0, len(letters_uppercase) - 1)]
        new_password.append(new_letter)
    
    for _ in range(nb_of_characters):
        new_letter = numbers[random.randint(0, len(numbers) - 1)]
        new_password.append(new_letter)
    
    for _ in range(nb_of_numbers):
        new_letter = symbols[random.randint(0, len(symbols) - 1)]
        new_password.append(new_letter)

    random.shuffle(new_password)

    return ''.join(new_password)

print(password_generator(10, None, None))