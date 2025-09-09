class NonIntArgumentException(Exception):
    pass

# Python code below
def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) is not int:
                raise NonIntArgumentException
        return func(*args)
    return wrapper

@handleNonIntArguments
def sum(*args):
    total = 0
    for arg in args:
        total += arg

    return total


try:
    sum(1,2, "spam")
except NonIntArgumentException as e:
    print(e)

try:
    sum(1,2, 3)
    print("sum did not throw exception")
except NonIntArgumentException as e:
    print("Should not have an exception here - FAIL!")

try:
    sum(None, None, None)
    print("this should not print out")
except NonIntArgumentException as e:
    print("PASSED!")
