# dict operations
data = {'a':1, 'b':2, 'c':3}

for k in data.keys():
    print(k)

for k in data.values():
    print(k)

t = (4, 5, 6)
x, y, z = t

print(x, y, z)

items = data.items()
print(items)

# -------------
person = {
    'name': 'khaled',
    'age' : 18,
    'hair_color' :'black'
}

changes = {
    'name': 'k1'
}

additional_infos = {
    'height': 6,
    'drink_coffee' : False
}

print(person)
person.update(changes)
print(person)

person.update(additional_infos)
print(person)

# -------------- coply dict
d1 = person.copy()
print(d1)

# ---------- default
person_2 = {
    'name': 'kevin',
    'age' : 18,
    'hair_color' :'black'
}

person_2.setdefault('height', 'N/A')
print(person_2)

