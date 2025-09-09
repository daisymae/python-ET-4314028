# Python code below
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)

def square(num):
    # my solution
    # squared = triangle(num) + triangle(num) - num
    # her solution
    squared = triangle(num) + triangle(num - 1)
    return squared


print(triangle(5))
print(square(5))

print(triangle(3))
print(square(3))

print(triangle(4))
print(square(4))

print(triangle(10))
print(square(10))