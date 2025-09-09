# Python code below
def factorial(num):
    # Your code goes here.
    print(type(num))
    if type(num) is not int or num <= 0:
        print("num is not int " + str(num))
        return None
    else:
        print("num is int " + str(num))
        if(num == 0):
            return 1
        else:
            n = num
            while n > 1:
                num = num * (n-1)
                n -= 1
                print("num is " + str(num))
                print("n is " + str(n))
            return num


number = 5
result = factorial(number)
print("factorial is " + str(result))

number = 6
result = factorial(number)
print("factorial is " + str(result))

number = 0
result = factorial(number)
print("factorial is " + str(result))

number = -2
result = factorial(number)
print("factorial is " + str(result))

number = 1.2
result = factorial(number)
print("factorial is " + str(result))

number = "spam spam spam spam spam spam"
result = factorial(number)
print("factorial is " + str(result))