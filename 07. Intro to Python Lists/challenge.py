# ----------------------------------------------------------------
# Copying all elements of a list into a new list

# Original list with mixed data types
my_list = [10, "hello", 3.14, True, None]
# Empty list to store copied elements
my_new_list = []

# Iterate through the original list using a for loop
for i in range(len(my_list)):
    my_new_list.append(my_list[i])

print(my_new_list)  # Output the new list
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# Function to retrieve an element from a list at a specific position
def get_elment_position(my_list: list, position: int):
    """
    Function to retrieve an element from a list at a given position.
    Args:
        my_list (list): The input list.
        position (int): The index of the element to retrieve.
    Returns:
        The element at the specified position.
    """
    return my_list[position]  # Return the element at the given position


# Call the function with position 1 and print the result
print(get_elment_position(my_list, 1))
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# Printing elements of the list in forward order
for i in range(len(my_list)):
    print(my_list[i])

# Printing elements of the list in reverse order
for i in range(
    len(my_list) - 1, -1, -1
):  # Start from the last index and move to the first
    print(my_list[i])
# ----------------------------------------------------------------
