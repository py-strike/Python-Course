


def create_counter():
    count = 0
    
    def display_counter():
        nonlocal count
        print(f"Counter = {count}")
        count += 1

    return display_counter

counter_func = create_counter()

counter_func()
counter_func()
counter_func()

# ---------------------------------------

