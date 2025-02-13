# 01
def calc(operation, *args):
    result = 0
    if(operation == "add"):
        for v in args:
            result += v
    elif (operation == "mult"):
        result = 1
        for v in args:
            result *= v

    return result

print(calc("mult", 1, 5 ,7))

# 02
def printy(msg, **kwargs):
    new_text = ",".join([f'{k}={v}' for k, v in kwargs.items()])

    print(msg + new_text)

printy("Hi ", **{'location':"skikda", 'weather':"sunny"})