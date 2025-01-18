# Sets {}
# Unique Values | Unordered | Mutable
my_nums = {1, 10, 44, 59, 12}

for n in my_nums:
    print(n)

# ---------------------
if 10 in my_nums:
    print("10 is in the set")
else:
    print("10 is not in the set")

my_nums.add("23")
print(my_nums)

my_nums.remove(44)
print(my_nums)

# ---------------------
my_nums_1 = {1, 10, 44, 59, 12}
my_nums_2 = {1, 11, 555, 666}

union =  my_nums_1 | my_nums_2
print(union)

intersection =  my_nums_1 & my_nums_2
print(intersection)

diffrence =  my_nums_1 - my_nums_2
print(diffrence)

symetrique_diffrence =  my_nums_1 ^ my_nums_2
print(symetrique_diffrence)
