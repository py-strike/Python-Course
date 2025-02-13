import random

def password_generator(lenght: int, charset: list, other_options):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_password = []

    for _ in range(lenght):
        new_letter = letters[random.randint(0, len(letters) - 1)]
        new_password.append(new_letter)

    return ''.join(new_password)

print(password_generator(10, None, None))