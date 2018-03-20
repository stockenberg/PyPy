from pprint import pprint as pp
from math import sqrt

word_list = ["Hallo", "du", "Dude"]
lengths = []


setlist = {"Hallo", "Test", "123", "asdasd"}
# comprehension in sets
setleng = {len(item) for item in setlist}


# List Comprehension
[len(word) for word in word_list]
# [expr(item) for item in iterable]
''' ist das selbe wie: '''
for word in word_list:
    lengths.append(len(word))


attribute_to_value = {
    'name': 'Mark',
    'age': 24,
    'gender': None
}

# items method if we want keys and values + tuple unpacking
# in case of duplicate keys: later overwrites the first
value_to_attribute = {attribute: value for value, attribute in attribute_to_value.items()}
pp(value_to_attribute)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


res = [x for x in range(101) if is_prime(x)]
prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}
print(res)
pp(prime_square_divisors)


iterable = ["Spring", "summer", "autumn", "winter"]

iterator = iter(iterable)
next(iterator)
# 'Spring'
next(iterator)
# 'summer'
next(iterator)
# 'autumn'
next(iterator)
# 'winter'
next(iterator)


def get_first_item(iterator_obj):
    iterator_obj_x = iter(iterator_obj)
    try:
        return next(iterator_obj_x)
    except StopIteration:
        raise ValueError("iterable is empty")
