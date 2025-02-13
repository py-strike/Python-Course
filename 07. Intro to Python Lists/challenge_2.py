def rotate(my_list: list):
    # TODO: Implement the rotate function to rotate the elements in the list
    # to the right by one position.
    # For example, rotate([1, 2, 3, 4, 5], 2) should return [4, 5, 1, 2, 3].
    # You can assume that the list will always have at least one element.
    my_list = (
        my_list[1:] + my_list[:1]
    )  # This line rotates the list to the right by one position.
    return my_list


print(rotate([1, 2, 3, 4, 5]))


# ----------------------------------------------------------------
def rotate_02(my_list: list, offset: int, direction: str):
    # TODO: Implement the rotate function to rotate the elements in the list
    # to the right or left by a specified number of positions.
    # For example, rotate([1, 2, 3, 4, 5], 2, "right") should return [4, 5, 1, 2, 3].
    # For example, rotate([1, 2, 3, 4, 5], 2, "left") should return [3, 4, 5, 1, 2].
    # You can assume that the list will always have at least one element.
    # You can assume that the offset will always be a non-negative integer.
    # You can assume that the direction will be either "right" or "left".
    if direction == "right":
        """offset = offset % len(my_list)"""
        my_list = my_list[-offset:] + my_list[:-offset]
    elif direction == "left":
        """offset = offset % len(my_list)"""
        my_list = my_list[offset:] + my_list[:offset]
    return my_list


print(rotate_02([1, 2, 3, 4, 5], 2, "left"))


# ----------------------------------------------------------------
def is_palindrome(list):
    # TODO: Implement the is_palindrome function to check if a given list is a palindrome.
    # A palindrome is a list that reads the same forwards and backwards.
    # For example, is_palindrome([1, 2, 3, 2, 1]) should return True.
    # For example, is_palindrome([1, 2, 3, 4, 5]) should return False.
    # You can assume that the list will always have at least one element.
    return list == list[::-1]


print(is_palindrome([1, 2, 3, 4, 5]))
print(is_palindrome([1, 2, 3, 2, 1]))
