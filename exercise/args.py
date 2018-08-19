# parameters packing #
def fun(a, *b, **c):
    print(a)
    print(list(b))
    print(list(c))


a = 1
b = (2, 3, 4)
c = {"x": 5, "y": 6}
fun(a, b, c)
fun(a, *b, **c)


# args unpacking #
def parrot(first, last, gender):
    print(first, last, gender)


args = {"first": "Muye", "last": "Zhang", "gender": "male"}
parrot(**args) # unpack dict
args = ("Yingyu", "Huang", "female")
parrot(*args) # unpack tuple


# lambda with closure #
def add(n):
    return lambda x: x + n


f = add(42)
print(f(0))
print(f(1))
