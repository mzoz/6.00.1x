


class myDict(object):
    """ Implements a dictionary without using a dictionary """
    class pair():
        def __init__(self, k, v):
            self.k = k
            self.v = v

        def __str__(self):
            return str(self.k)

        def __eq__(self, other):
            return self.__str__() == other.__str__()

        def __hash__(self):
            return self.k

        def get(self):
            return self.v

        def update(self, v):
            self.v = v


    def __init__(self):
        """ initialization of your representation """
        self.dict = set()

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if k in self.dict:
            for key in self.dict:
                if key == k:
                    key.update(v)
        else:
            self.dict.add(self.pair(k, v))

    def getval(self, k):
        """ k, immutable object  """
        if k not in self.dict:
            raise KeyError
        for key in self.dict:
            if key == k:
                return key.get()

    def delete(self, k):
        """ k, immutable object """
        if k not in self.dict:
            raise KeyError
        self.dict.remove(k)


d1 = myDict()
d1.assign(1,2)
d1.assign(3,4)
d1.assign(3,5)
print(d1.getval(3))


# only looking for a KeyErrors
'''
d1 = myDict()
d1.assign(2, 3)
print(d1.getval(2))
print(d1.getval(3))
d1.assign(3, 3)
print(d1.getval(3))
print(d1.getval(2))
d1.assign(4, 2)
d1.delete(3)
print(d1.getval(2))
d1.delete(10)
d1.delete(3)
d1.assign(6, 1)
print(d1.getval(6))
'''