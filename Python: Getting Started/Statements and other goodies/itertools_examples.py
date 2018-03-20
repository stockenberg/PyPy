from itertools import islice, count

thousand= islice((x for x in count()), 1000)
print(thousand)

print(list(thousand))

any([False, True, True])
# True

all([False, True, True])
# False

# check if all is uppercase
print(all(name == name.title() for name in ['London', "Stuttgart", "Berlin"]))


sunday = [12, 14, 15, 16, 17, 18]
monday = [13, 14, 15, 14, 15, 12]

# Zip yields tuples
for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print(sun)
    print(mon)


# min(), max(), sum(), len(), chain() <-- from itertools
