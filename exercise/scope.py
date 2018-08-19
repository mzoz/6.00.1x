var = 1


def change_var():
    global var
    var = 42


def print_var():
    print(var)


print_var()
change_var()
print_var()
