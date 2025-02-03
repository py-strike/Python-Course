# Selection Sort
def selection_sort(nb):
    sorted_nb = []

    for _ in range(len(nb)):
        next_min = min(nb)
        sorted_nb.append(next_min)
        
        nb.remove(next_min)
    
    return sorted_nb

print(selection_sort([4, 101, -40 ,44, 8, 9, 9, -41, 12]))






























