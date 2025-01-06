x = 6
message = "hello"


def what_is_X():
    x = 10

    def nested_func():
        x = 11
        print(f"X is {x}")

    nested_func()
    print(f"X is {x}")


what_is_X()

print(f"X is {x}")

# ---------------------- global keyword
count = 0

def increment_count():
    global count
    count += 1

def reset_count():
    global count
    count = 0

def increment_count_by_5():
    global count
    count += 5

increment_count()
increment_count()
increment_count()
increment_count()
print(count)

reset_count()
print(count)

increment_count_by_5()
print(count)

# more sophisticated approch
def modify_count(command): # inc, reset, big_inc
    staring_value = 0
    inc_value = 1
    big_inc_value = 10

    def inc():
        global count
        count += 1

    def reset():
        global count
        count = 0

    def big_inc():
        global count
        count += big_inc_value

    def change_big_inc_value(new_value):
        nonlocal big_inc_value
        big_inc_value = new_value

    if command == 'inc':
        inc()
    elif command == 'reset':
        reset()
    elif command == 'big_inc':
        big_inc()
    elif command == 'change_bic_inc':
        change_big_inc_value(5)

modify_count('inc')
modify_count('inc')
modify_count('inc')
modify_count('inc')
modify_count('inc')
modify_count('inc')
print('count : ' + str(count))

modify_count('reset')
print('count : ' + str(count))

modify_count('big_inc')
print('count : ' + str(count))

modify_count('change_bic_inc')
modify_count('big_inc')
print('count : ' + str(count))