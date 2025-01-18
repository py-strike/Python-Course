my_tuple = (1, 2, "Salem", 5)
print(my_tuple[1])

one_elemnet_tuple = (1,)

# ----------------------
tuple_01 = (1,2,5,6,5,1,1,1,10)
print(f"number of 1's : {tuple_01.count(1)}")
print(f"the first index of 1 is : {tuple_01.index(1)}")

# ----------------------
simple_tuple = ('a','b','c','d', 'e')
for l in simple_tuple:
    print(l)

print(list(simple_tuple))

upper_tiple = tuple(x.upper() for x in simple_tuple)
print(upper_tiple)