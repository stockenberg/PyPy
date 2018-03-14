def test(*args):
    for arg in args:
        print(arg)


test("hallo", "test", 1234)


def test2(**kwargs):
    print(kwargs)


test2(test="hallo", huhu="test")


def function_with_args(value, argument="Test", more="test"):
    print(value)
    print(argument)
    print(more)


function_with_args(1, "assd", more="asdasd")

print("Hello", "world", 3, None, "Something")
