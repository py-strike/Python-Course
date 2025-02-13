def count_carachters(text):
    my_dictionary = {}
    for c in text:
        if c in my_dictionary:
            my_dictionary[c] = my_dictionary[c] + 1
        else:
            my_dictionary[c] = 1
    
    return my_dictionary

print(count_carachters("khaleddH"))
