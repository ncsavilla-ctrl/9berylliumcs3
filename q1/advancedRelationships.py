class ParentClass:
def __init__(self, value):
self.value = value

class ChildClass(ParentClass):

def __init__(self, value, extra):
super().__init__(value)
self.extra = extra
