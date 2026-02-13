#"Day 2: 30 Days of python programming" 

#variables in python
first_name = 'relpa'
last_name = 'dalla'
city = 'Amsterdam'
age = 15
is_married = False

skills = ['HTML', 'CSS',
          'JS', 'Java', 'python']
person_info = {
    'first_name' : 'relpa',
    'last_name' : 'dalla',
    'country':'Netherlands',
    'city': 'Amsterdam'
    }
print(len(person_info))
print(len('Hello, World!'))

#printing the values stored in the variables
print("First Name:",first_name)
print('first name length:',len(first_name))
print("last name:",len(last_name))
print(last_name)
print ("country: ", person_info['country'])
print("Age:", age)
print("Married: ", is_married)
print("skills: ", skills)
print("personal information: ", person_info)
#declaring multiple varaibles in a line

first_name, last_name, age, is_married = "relpa", "dalla", 16, False

print(first_name, last_name, age, is_married)
print("first_name: ", first_name)
print("last_name: ", last_name)
print("Age: ", age)
print("married: ", is_married)
#getting user input using the input()_built in function.let us assign the we get from a user into first_name and age variables.

first_name = input("what is your name? ")
age = input("How old are you? ")
print(first_name)
print(age)

#different data types in python
first_name = "relpa"
#str
last_name = "dalla"
#str
city = "amsterdam"
#str
age = 16
#int
#printing out types

print(type(first_name))#str 
print(type("relpa"))#str
print(type(16))#int/checking type with argument
print(type(age))#int/checking with variable
print(type(3.4))#float
print(type(1 + 3j))#complex
print(type(True))#bool
print(type([1, 2, 3, 4, 5]))#list
print(type({1, 2, 3, 3, 5}))#set
print(type({"salary": "$500"}))#dict
print(type((1, 2, 3, 4 ,5 ,6)))#tuple
print(type(zip([1,2],[3,4])))#zip

#casting or converting data types vice-versa(int to float , float to int etc..)

#int to float
num_int = 10
print("num_int", num_int)
num_float = float(num_int)#creating variable to change
print("num_float: ", num_float)
#float to int
gravity = 9.8
print(int(gravity))
#straight, use the desired data type to change

#int to str
num_int = 10
print(num_int)
#str to int or float
num_str = str(num_int)
print(num_str)
#convert the string to a float first
num_str = "10.6"
num_float = float(num_float)
print(num_float)
num_int = int(num_float)
#then convert the float to an integer
num_str = "24"
print("num_int: ", int(num_str)) #10
print("num_float:", float(num_str))#10.0
num_int =int(num_float)
print("num_int: ", int(num_int)) #10

#str to list
first_name = "relpa"
print(first_name)

first_name_to_list = list(first_name)
print(first_name_to_list)
#['r', 'e', 'l', 'p', 'a']

#number data types in python

#1:integer referes to negative,zero and positive numbers. eg:1, 0, -8, 8...

#2:floating point number refers to decimal numbers. eg:-1.5, 4.56, -1.2, 0...

#3:complex numbers refers to numbers that has two parts.eg:a+bj == 1+4j...











