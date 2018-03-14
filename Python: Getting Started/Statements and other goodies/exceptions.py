
student = {"test": "value"}

student['hallo'] = "yuuha"

try:
    hallo = student['hallo']
    test = 3 + hallo
except KeyError:
    print("error")
except TypeError as e:
    print("type error")
    print(e)
except Exception:
    print('Unknown error')

print("this happens..")