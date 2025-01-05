# Keys or Values can be anything
my_dictionary = {
    "name": "khaled",
    "age": 22,
    "love_python": True,
    "height": "1.77 cm",
}

print(my_dictionary["name"])
print(my_dictionary["age"])
print(my_dictionary["love_python"])

print(my_dictionary.get("j", "N/A"))

if "height" in my_dictionary:
    print("This Person's height is : " + str(my_dictionary["height"]))
else:
    print("This Info is not Available.")

# ----------------------------------------------------------------
my_dictionary["height"] = "1.78 cm"
print("Updated Height : " + my_dictionary["height"])

# ----------------------------------------------------------------
for key in my_dictionary:
    print(key + ": " + str(my_dictionary[key]))

# ----------------------------------------------------------------
for key, value in my_dictionary.items():
    print(key + ": " + str(value))
