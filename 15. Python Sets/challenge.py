def make_set(l:list):
    dict_set = {}
    for i,item in enumerate(l):
        dict_set[i] = item
    return dict_set

def add_to_set(d:dict, value):
    d[len(d)] = value
    return d

def discard_from_set(d:dict, value):
    for i,v in d.items():
        if v == value:
            d.pop(i)
            break
    return d

print(make_set([10, 52, 44, 75]))
print(add_to_set({"0":1, "1":74}, 55))
print(discard_from_set({"0":1, "1":74}, 74))