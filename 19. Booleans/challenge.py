def any_have_value(ls, key, value):
    values = [x.get(key, None) for x in ls]
    return any([v == value for v in values])


# ----------------------
def all_than(ls, number: int):
    return all([x > number for x in ls])

print(all_than([5, 2, 10, 11], 8))
    