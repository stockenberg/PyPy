def test(*args):
    ''' Accepts N Value Arguments as tuple'''
    for arg in args:
        print(arg)


test("hallo", "test", 1234)


def test2(**kwargs):
    ''' Accepts N-Key Arguments'''
    print(kwargs)


test2(test="hallo", huhu="test")


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    pass


print_args(1, 2, 3, kwarg1=4, kwarg2=5, custom_kwarg="test")


def function_with_args(value, argument="Test", more="test", *args, **kwargs):

    '''
    :param value: mixed This is a Param
    :param argument: string this is a scnd param
    :param more: integer more params
    :return: Void
    '''

    print(value)
    print(argument)
    print(more)


function_with_args(1, "assd", more="asdasd")

print("Hello", "world", 3, None, "Something")

''' EXTENDED CALL SYNTAX '''

t = (1, 2, 3, 4)
tkey = {"red": "test", "green": "test"}
test(*t)
test2(**tkey)


'''Forwarding Arguments'''


def trace(pre_defined_function, *args, **kwargs):
    result = pre_defined_function(*args, **kwargs)
    return result()


multilist = [[1,2,3,4], [5,6,7,8], [9,0,1,2]]
for item in zip(*multilist):
    print(item)
