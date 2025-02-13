def get_words(my_str: str):
    return my_str.split(" ")


print(get_words("Salem Alikoum."))


def capitalize(my_str: str):
    first_letter = my_str[0]
    rest_of_letters = my_str[1:]

    return first_letter.upper() + rest_of_letters.lower()


print(capitalize("salem."))


def capitalize_words(msg: str):
    result = ""
    for word in get_words(msg):
        result += capitalize(word) + " "
    return result


print(capitalize_words("salem alikoum."))
