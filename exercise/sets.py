class IntSet:
    def __init__(self):
        self.vas = []

    def insert(self, e):
        if e not in self.vas:
            self.vas.append(e)

    def member(self, e):
        return e in self.vas

    def remove(self, e):
        try:
            self.vas.remove(e)
        except:
            raise ValueError(str(e), "not found")

    def __str__(self):
        self.vas.sort()
        return self.vas.__str__()


a = IntSet()
a.insert("z")
a.insert("m")
a.insert("y")
print(a)
