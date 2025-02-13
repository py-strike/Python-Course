# exo 01
def reverse_halves(my_list):
    midpoint  = int(len(my_list) / 2)
    first_half = my_list[:midpoint]
    last_half = my_list[midpoint:]

    return [*last_half, *first_half]

print(reverse_halves([1,2,5,10]))

# exo 02
def apply_defaults(d, default):
    # return default | d
    return {**default, **d}

print(apply_defaults({'a':100, 'c':55}, {'a':1, 'b':2}))

# exo 03
def uppercase_keys(d):
    return [key.upper() for key in d.keys()]

print(uppercase_keys({'a':100, 'c':55}))

# exo 04
def squares_map(num):
    return { x:x * x for x in range(1, num+1) }

print(squares_map(4))