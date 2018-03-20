# Functions that behaves like iterators can be used within a for loop

def gene():
    yield 1
    yield 2
    yield 3


g = gene()
print(g)

for item in g:
    print(item)

for item in gene():
    print(item)


# code will be executed if iterated
def newgen():
    print("About to Yield2")
    yield 2
    print("About to Yield4")
    yield 4
    print("About to Yield6")
    yield 6


g = newgen()
next(g)
next(g)
next(g)


# Yield keyword returns an Item without stopping the loop - you can yield single items instead of returning whole lists
def take(count, iterable):
    counter = 0
    for itemm in iterable:
        if counter == count:
            return
        counter += 1
        yield itemm


# generator comprehensions
million_squares = (x*x for x in range(1, 1000))
