
string = 'Hello'
string_2 = "Hello!"
string_3 = """HELLO"""


string.capitalize()
string.replace("e", "a")
string.isalpha() #bool
string.isdigit() #bool
list = string.split('l')


sentence = "NIce to Meet you {0} iam {1}".format(string, string_2)

print(sentence)

#print(f"Nice to meet {string}") not supported by python3.5