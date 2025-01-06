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
