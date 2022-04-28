import constant
import numeric
import string
import boolean
import special
import literal_collection

# Python Variables
number = 10
number = 1.1

# Declaring and assigning value to a variable
website = "https://upcolor.weblike.jp/portfolio-1/"
print (website)
website = "www.google.com"
print (website)

# Assinging multiple values to multiple variables
a , b, c = 2, 3.2, "Hello"
print (a)
print (b)
print (c)

# Assinging same values to multiple variables
x = y = z = "same"
print (x)
print (y)
print (z)

# Declaring and assigning value to a constant form 'constant.py'
print(constant.PI)
print(constant.GRAVITY)

# Numeric literals in Python
print(numeric.binary, numeric.decimal, numeric.octal, numeric.hexa)
print(numeric.float_1, numeric.float_2)
print(numeric.x, numeric.x.imag, numeric.x.real)

# String literals in Python
print(string.strings)
print(string.char)
print(string.multiline_str)
print(string.unicode)
print(string.raw_str)

# Boolean literals in Python
print("x is", boolean.x)
print("y is", boolean.y)
print("a:", boolean.a)
print("b:", boolean.b)

# Literals Collection in Python
print(literal_collection.fruits)
print(literal_collection.numbers)
print(literal_collection.alphabets)
print(literal_collection.vowels)