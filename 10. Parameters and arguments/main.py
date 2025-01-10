# Positional ARGUMENTS / keywork ARGUMENTS

def add(a, b, c):
    print(f"a is {a}")
    print(f"b is {b}")
    print(f"c is {c}")
    return a+b+c

print(add(1, 5, 8))
print(add(b=1, c=5, a=8))