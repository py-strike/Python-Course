import random

fruits = [
    "apple", "banana", "orange", "grape", "strawberry",
    "blueberry", "kiwi", "mango", "pineapple", "watermelon",
    "peach", "pear", "plum", "cherry", "raspberry"
]

random_index = random.randint(0, len(fruits) - 1)
word_to_guess = fruits[random_index]

print(word_to_guess)

def get_spaces_and_letters(word_to_guess, user_guess):
    scpaces_and_letters = ""

    for letter in word_to_guess:
        if letter in user_guess:
            scpaces_and_letters += f" {letter} "
        else:
            scpaces_and_letters += " _ "
    
    return scpaces_and_letters
    
def get_next_guess(guesses):

    while True:
        user_guess = input("Enter your guess : ")
        if len(user_guess) != 1:
            print("Only enter a single character.")
        elif user_guess in guesses:
            print("You've already guess this character.")
            # break
        else:
            return user_guess.lower()
        
def is_loss(word, guesses):
    ...

def is_win(word, guesses):
    ...

def is_corrrect_guess(word, guesses):
    return new_guess in word

turn_left = 7
guesses = []

while turn_left > 0:
    print(f'you have {turn_left} turns left.')
    print(get_spaces_and_letters(word_to_guess, guesses))
    new_guess = get_next_guess(guesses)
    guesses.append(new_guess)

    if not is_corrrect_guess(word_to_guess, new_guess):
        print("that was an incorrect guess.")
        turn_left -= 1
    else:
        print("that was a correct guess.")
