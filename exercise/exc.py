def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")


def fancy_divide4(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)


def fancy_divide5(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)


# tut p62 except catch super class
# 25-7-2018
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")


for cls in [B, C, D]:
    try:
        raise cls
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

try:
    raise Exception("m", "z")
except Exception as exc:
    print(type(exc))
    print(exc.args)
    print(exc)
    x, y = exc.args
    print(x, y)
else:
    print("not showing unless no exception caught")

try:
    try:
        raise NameError("mz")
    except NameError:
        print("** an error just flew by!")
        raise
except NameError:
    print("** catch it!")


class Error(Exception):
    def __init__(self, *args):
        self.args = list(args)


try:
    raise Error("a", "b", 42)
except Error:
    print("error caught")
