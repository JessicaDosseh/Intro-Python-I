"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# % is the string modulo operator read more about it: https://www.python-course.eu/python3_formatted_output.php

print("The value of %(x)s is ten, the value of %(y)s is a decimal, and the value of %(z)s is <3 turtles."
      % {'x': x, 'y': y, 'z': z})

# Use the 'format' string method to print the same thing

# "{}". format(value)read more about it: https://pyformat.info/
print("The value of {} is ten, the value of {} is a decimal, and the value of {} is <3 turtles.".format(x, y, z))

# Finally, print the same thing using an f-string
# SyntaxError: invalid syntax why?
print(
    f"The value of {x} is ten, the value of {y} is a decimal, and the value of '{z}' is <3 turtles.")
