# Syntax Error
# Indentation Error
# ----------------------
# Type Error
# Value Error
# Name Error
# Index Error
# Key Error
# Zero Division Error

# Raising errors
def repeat_striung(s, nb_of_rep):
    if type(s) is not str:
        raise TypeError('The text must be a strings')
    
    if type(nb_of_rep) is not int:
        raise TypeError('The nb of rep must be an integer')

    return s*nb_of_rep

s = input("Enter a text to be repeted : ")
nb_of_rep = int(input("Enter the number od repetetion : "))

print(repeat_striung(s, nb_of_rep))