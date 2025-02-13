try :
    raise TypeError("Oh no!")
except Exception as e:
    if type(e) is ValueError:
        print("value error")
    elif type(e) is TypeError:
        print("type error")
