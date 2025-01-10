# Positional ARGUMENTS / keywork ARGUMENTS

def add(a, b, c):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    return a+b+c

print(add(1, 5, 8))
print(add(b=1, c=5, a=8))

# ---- putting restrictions on positional / keyword arguments

def add_v2(a, b, c, /, *, d, e, f):
    return a+b+c+d+e+f

print(add_v2(5, 4, 1, d=10, e=12, f=9))

# ---- default argument

def repeat_string(s, nb_repeat=2):
    return s * nb_repeat

print(repeat_string("Hi", 4))

# ---- Arbitrary argument

def add_v3(*args):
    total = 0
    for v in args:
        total += v
    return total

print(add_v3(1, 2, 4))