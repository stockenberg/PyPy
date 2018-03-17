
import os

student = {"test": "value"}

student['hallo'] = "yuuha"
x = 1

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
except (Exception, TypeError, KeyError):
    pass
     # reraise the exception message

print("this happens..")

if x < 0:
    raise ValueError("Cannot do it")


p = '/path'

try:
    t = ""
    # process_file(f)
except OSError as e:
    print("error in {}".format(e))


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e)
        raise
    finally:
        os.chdir(original_path)

