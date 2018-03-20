class Empty:
    pass


## Methods are just functions in classes
# instance methods are functions with the self keyword - can be called from an instance

class InitializerClass:

    # no constructor - initializer
    def __init__(self):
        # instance Attribute is private by _ (convention)
        self._argument = "Test"
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


class PolyMorph(AB):

    def __init__(self):
        AB.__init__(self)

    def func(self):
        pass

    def scndfunc(self):
        original_value = super().func()
        pass


# instance without new keyword
test = AB("arg")
test.cry_me_tears()

