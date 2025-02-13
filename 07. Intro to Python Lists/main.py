# Into du Python Lists

numbers1 = [1, 2, 3, 4, 5]
my_list = [10, "hello", 3.14, True, None]
fruits = ["apple", "banana", "orange", "grape", "mango"]

print(numbers1)
# access the first item in the list
print(fruits[0])

# loop trough a list
for f in fruits:
    print(f)

# modify a list
fruits[1] = "kiwi"
print(fruits)

# add an item
fruits.append("Fig")
print(fruits)

# size of a list
print(f"we have a total of {len(fruits)} fruits.")

# get the last element
print(f"Our most recent fruits is {fruits[len(fruits) - 1]}.")

# or this annotation
print(f"Our most recent fruits is {fruits[-1]}.")

# slice the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:5])
print(numbers[-2:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])
