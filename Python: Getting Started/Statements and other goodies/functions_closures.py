''' Remembers the objects from local scope need for execution'''


def enclosing():
    x = 'closed over'

    def local_func():
        return x + " localstuff"
    return local_func()


def enc():
    x = 'to be changed in local func'

    def local():
        nonlocal x  # x can be changed now - referenced to line 12
        x = "test"
        return x

    local()

lf = enclosing()
print(lf)

'''in reppl'''
# print(lf.__closure__)

