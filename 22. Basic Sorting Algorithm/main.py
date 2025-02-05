# Selection Sort
def selection_sort(nb):
    sorted_nb = []

    for _ in range(len(nb)):
        next_min = min(nb)
        sorted_nb.append(next_min)
        
        nb.remove(next_min)
    
    return sorted_nb

print(selection_sort([4, 101, -40 ,44, 8, 9, 9, -41, 12]))

# Bubble Sort
my_list_to_sort = [4, 101, -40 ,44, 8, 9, 9, -41, 12]

def bubble_sort(my_list):
    for _ in my_list:
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                a = my_list[i + 1]
                my_list[i + 1] = my_list[i]
                my_list[i] = a
                
    return my_list

print(bubble_sort(my_list_to_sort))

# Insertion sort
def inserction_sort(original_list: list):
    my_list = original_list.copy()
    sorted_numbers = []

    for x in my_list:
        was_inserted = False
        for i in range(len(sorted_numbers)):
            if sorted_numbers[i] > x:
                sorted_numbers.insert(i, x)
                was_inserted = True
                break

        if not was_inserted:
            sorted_numbers.append(x)

    return sorted_numbers

my_list_to_sort_2 = [4, 101, -40 ,44, 8, 9, 9, -41, 12, 111, -200]
print(f"Insertion Sort : {inserction_sort(my_list_to_sort_2)}")






























