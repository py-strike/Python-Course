# 01 ----------------------------------------------------------------
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"a": 3, "d": 4}


def combine(d1, d2):
    for k, v in d2.items():
        d1[k] = v
    return d1


print(combine(d1, d2))


# 02 ----------------------------------------------------------------
def combine_v2(d1, d2):
    for k, v in d2.items():
        if k in d1.keys():
            print("The dicionarie must have diffrente keys.")
            return {}
        d1[k] = v

    return d1


print(combine_v2(d1, d3))


# 03 ----------------------------------------------------------------
def access_entery(d1, name):
    return d1.get(name, "This Key D'ont existe")


print(access_entery(d1, "a"))
