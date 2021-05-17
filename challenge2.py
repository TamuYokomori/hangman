# challenge 2

# receive a number as a input value, and return 2 squared value of the number.

def f(x):
    return(x ** 2)

print(f(3))


# set a string as a argument, output the string.

def print_string(string):
    print(string)

print_string('Testing: 1, 2, 3')


# 3 required and 2 optional argument.

def f(x, y, z, a=3,b=4):
    return a * b + (x + y + z)

result = f(3, 5, 10)
print(result)


# a program consists of 2 function.
# one function receives a integer as argument, and output a integer derived from the integer devided by 2.
# another receives as well, and return the integer multiplied by 4.
# reserve the former returned value, and pass itself as an argument of the second function.

def divide(x):
    return x / 2

a = divide(100)
print(int(a))


def multiple(x):
    return x * 4

b = multiple(a)
print(int(b))


# convert a string to float type and return.
# catch exceptions that can happen.

def convert(string):
    try:
        return float(string)
    except ValueError:
        print('Could not convert the string to a float')

c = convert('55.0')
print(c)

d = convert('python')
print(d)


