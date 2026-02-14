#day 3
###boolean is a data type that represents True and False, the first letter of True and False should be capital.
print(True)
print(False)

# there are lots of operators in python programing language.
#assignment operators are used to assign values to variables: eg x = 5, unlike mathematics, 3 = 3, equal sign is used to assign in python and not to show equivalence, assign means to store a value(5) in a vairable x.

## arithemetic operations in python
#integers
print("addition: ", 3 + 4)
print("subtract: ", 7 - 3)
print("divide: ", 8 / 2)
print("exponent: ", 6 ** 2)
print("floor division: ", 33 // 2)
print("modulos: ", 8 % 6)# gives remainder
print("multiply: ", 6 * 3)

#floating numbers
print("float point number, height :", 170.8)
print("float number, body temperature: ", 37.2)

#complex numbers 
print("complex number: ", 2 + 3j)
print("multiply complex number: ", 2 + 3j * 3 + 5j)

# do not use variable names that are vague , always keep it mnemonic and descriptive to the context.

#rule of thumb: we must declare variable upfront just like declaring your stuffs at airpot and then only you get to board the flight, in pyhon if we do not declare the variable , we will get errors and cant procced.

car = 3 # car is a variable name and 3 is an int dtype.
penthouse = 4

#arithemetic operations and assigning the result to a variable
total = car + penthouse
diff = car - penthouse
product = car * penthouse
division = car / penthouse
remainder = car % penthouse
exponent = car ** penthouse
floor_division = car // penthouse

print(total)# if we just print, we will not be able to identify the source of the result and for that we have to label with a string.
print("car + penthouse: ", total )
print("car - penthouse: ", diff)
print("car * penthouse: ", product)
print("car / penthouse: ", division)
print("car % penthouse: ",remainder)
print("car ** penthouse: ", exponent)
print("car // penthouse: ", floor_division)

#declaring values and organizing them together
car = 3
penthouse = 4
#arithemetic operations
total = car + penthouse
diff = car - penthouse
product = car * penthouse
division = car / penthouse

# printing result with labels
print("total: ", total)
print("diff: ", diff)
print("product: ", product)
print("remainder: ", remainder)

#apply the knowledge to calculate(area, volumem density , weight , perimeter distance, force).lets go

#calculating the area of circle.
# we know the formula to find the area of cirlce is PIR2(r squared)

pi = 3.14
radius = 3
area_of_circle = pi * radius ** 2
print("area_of_circle: ", area_of_circle)

# calculating the area of rectangle
length = 10
width = 5
area_of_rectangle = length * width
print("area_of_rectangle : ", area_of_rectangle)

#calculating a weight of an obeject
mass = 58
gravity = 9.81
weight = mass * gravity
print("weight,'N': ", weight)
# adding unit to weight. 'N' means Newton.

#calculating the desity of a liquid.
mass = 65 # in kg
volume = 0.074 #in cubic meter
density = mass / volume
print("density: " , density)

#comparison operators: in python we compare two values, if its greater ,less, or equal to other value.

print(3 > 2)
print(7 < 8)
print(6 >= 5)
print(4 <= 5)
print(3 == 2)
print(3 != 6)
print(len('fruit') == len('vegetables'))
print(len('bottle') == len('table'))
print(len('cat') == len('dog'))

print("True == True: ", True == True)
print("True == False: ", True == False)

print("1 is 1: ", 1 is 1)
print("2 is not 3: ", 2 is not 3)

print("r in relpa: ", 'r' in "relpa")
print("z is not in relpa: ",'z' not in "relpa" )
print("wisdom" in "wisdom is a gem")

#logical operators: python also used keywords 'and' 'or' and 'not'. they are used to combine conditional statements.
print(3 > 2 and 4 > 3)
print(4 > 3 and 6 < 3)
print("True and True: ", True and True)
print("True and False: ", True and False)
print(3 > 2 or 4 > 3)
print(3 < 2 or 4 < 3)
print("True or False: ", True or False)
print(not 3 > 2)
print(not True)
print(not False)
print(not not True)























