class Person:
    def __init__(self, name):
        __name__ = name
        print(__name__)

    def getAge(self):
        print(__name__)


p = Person('John')
p.getAge()
p.__init__('Merry')
