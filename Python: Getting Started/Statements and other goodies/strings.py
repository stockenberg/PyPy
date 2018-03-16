
string = 'Hello'
string_2 = "Hello!"
string_3 = """HELLO"""

seperator = ";"

joins = seperator.join(["2","3","4"])
print(joins)

splits = joins.split(";")
print(splits)

origin, _, destination = "Seattle-Boston".partition('-')

"The age of {0} is {1}".format("Jim", 3)
"The age of {} is {}".format("Jim", 3)
"The age of {0} is {1} and {0} is cool".format("Jim", 3)
"Named {field} is also possible".format(field="popser")

pos = (10, 20, 30)
"Galatic position x = {pos[0]}, y = {pos[1]}, z = {pos[2]}".format(pos=pos)

''.join(["Ma", "rt", "en"])  # use this for concatination

string.capitalize()
string.replace("e", "a")
string.isalpha() #bool
string.isdigit() #bool
list = string.split('l')




sentence = "NIce to Meet you {0} iam {1}".format(string, string_2)

print(sentence)

#print(f"Nice to meet {string}") #not supported by python3.5
