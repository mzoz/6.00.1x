def outer(msg):
    def inner():
        print(msg)
    return inner


# local variable detained after function call
fun = outer("hello")
fun()
