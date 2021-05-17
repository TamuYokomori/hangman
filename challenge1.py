# output three different strings.

print('No.1')
print('No.2')
print('No.3')


# output a message when the variable is less than 10, or a defferent message when greater than or equal to 10.

x = 1

if x < 10:
    print("x is less than 10.")
else:
    print('x is greater than or equal to 10.')


# output a message when the variable is less than or equal to 10.
# a defferent message when greater than 10, but less than or equal to 25.
# even more a  different message when greater than 25.

y = 22

if y <= 10:
    print('y is less than or equal to 10.')
elif 10 < y <= 25:
    print('y is greater than 10, but less than or equal to 25.')
else:
    print('y is less than 25.')


# divide two values and output the surplus.

14 % 3


# divide two values and output the quotient.

14 // 3


# substitute an integral for the variable 'age', and execute some condition branching by using 'age'.
# output in accordance with conditions.

age = 11
adult_permission = age - 18 
z = adult_permission

if z < 0:
    print("You have no right to access to this web page.")
else:
    print("You have a right to access to this web page.")
