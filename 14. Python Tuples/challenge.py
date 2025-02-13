def index_all(t:tuple, myindex:int):
    my_indexes = [] 
    for i, item in enumerate(t):
        if item  == myindex:
            my_indexes.append(i)
    
    return my_indexes

print(index_all((1, 5, 8, 10, 1), 1))

# -------------------

def append_tuple(t:tuple, item):
    return (*t, item)

print(append_tuple((1, 5, 8, 10, 1), 444))

# -------------------
def insert_tuple(t:tuple, index:int, item):
    f_half = t[:index]
    l_half = t[index:]

    return f_half + (item,) + l_half

print(insert_tuple((1, 5, 8, 10, 1), 2, 444))
