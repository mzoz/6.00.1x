def beautify(girl):
    def inner():
        print("beautiful ", end="")
        girl()
    return inner


@beautify
def asian():
    print("asian girl")


def white():
    print("white girl")


def latin():
    print("latin girl")


beautify(asian)()
beautify(white)()
'''
output:
beautiful beautiful asian girl
beautiful white girl
'''