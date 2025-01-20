u = input("Enter a number : ")

try:
    number = int(u)
    print(f"the num you entred plus one is : {number + 1}")
except ValueError:
    print("Is not a number")

u2 = input("Enter a number : ")

try:
    number = int(u2)
    print(f"the num you entred minus one is : {number - 1}")
except Exception: # generic type of exception
    print("This is not a number")