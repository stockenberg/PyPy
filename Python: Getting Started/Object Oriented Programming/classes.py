class Empty:
    pass


class ConstructorClass:

    def __init__(self):
        # instance Attribute
        self.argument = "Test"
        pass


class Members:
    # class Attributes
    i = None
    a = []
    b = {}
    c = False
    d = "String"
    pass


class Test:

    def __init__(self):
        print("Test Class")

    @staticmethod
    def cry_me_tears():
        print("tears")
        Test.test()

    @staticmethod
    def test():
        pass


# Inheritance
class AB(Test):

    def __init__(self, arg=None):
        Test.__init__(self)
        # constructor
        print('test')
        print(arg)
        pass

    def func(self):
        pass

    def scndfunc(self):
        self.func()


# instance without new keyword
test = AB("arg")
test.cry_me_tears()

