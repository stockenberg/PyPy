number = 5

if number == 5:
    print("Number == {0}".format(number))
else:
    print("nein!")


if number:
    print("Number is defined and truthy")


text = "Python"
if text:
    print("Text is defined and truthy")


boolean = True
if boolean:
    print("True")

none = None
if none:
    print("Will NOT executed")


if not boolean:
    print('stuff')

if number == 3 and bool:
    pass

if number == 17 or bool:
    pass


a = 1
b = 2

outcome = "bigger" if a > b else "smaller"

print(outcome)