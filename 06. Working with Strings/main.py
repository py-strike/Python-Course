# Workikng with strings

print("Hello".upper())
print("Hello".lower())
print("    Hello   ".strip())

my_str = "Hello, Khaled"
print(my_str.replace("Hello", "Hi"))

my_str_2 = "Apple,Banana,Orange,Grape,Strawberry"
print(my_str_2.split(","))

print(my_str_2.startswith("App"))
print(my_str_2.endswith("khaled"))
print("Orange" in my_str_2)
