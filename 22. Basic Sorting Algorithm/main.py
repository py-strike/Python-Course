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






























