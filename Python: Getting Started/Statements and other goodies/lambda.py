

## anonymous funcs



two = lambda:  2
double = lambda parameter: parameter * 2
double_threeargs = lambda parameter, param2, param3: parameter * 2

print(double(15))

data = ['Person1', 'Person2', 'Person3', 'Person4']

sorted(data, key=lambda name: name.split()[-1])