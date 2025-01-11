a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

a.extend(b)
print(a)

# Unpacking the list with "*" 
d = [0 , *a,-100, 18]
print(d)

# Unpacking dictionaries
d1 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

d2 = {
    'd': 4,
    'e': 5,
    'f': 6,
}

d3 = {
    'a': 100,
    'c': 18,
    'f': -4,
}

print( d1 | d2 | d3)

d4 = {
    **d1,
    'b': 100,
    **d2
}

print(d4)

# List comprehension
num = [1,2,3,4,5]

num_2 = [ x*2 for x in num]
print(num_2)

num_3 = [ x for x in num if x%2 == 0]
print(num_3)

people = [{'name':'a', 'age': 21}, {'name':'b', 'age': 25}, {'name':'c', 'age': 34}]
names = [p['name'] for p in people]
print(names)

# dictionary comprehension
d_11 = {key.upper(): value*2 for key, value in d1.items()}
print(d_11)