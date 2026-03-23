#day 4 : strings
#every text is a string data type in python , its enclosed in single, double and triple quotes, there are many ways to deal with string datatypes and we can check the len of the string with len() function

#creating a string 
letter = 't'
print(letter)
print(len(letter))
greeting = "hello, world"
print(len(greeting))
print(greeting)
sentence = "i am very glad to learn python"
print("string: ", sentence)

#multiline string is created by usint triple single quotes(''') or triple double quotes("""). lets have some examples below.

multiline_string = '''i am a student of computer science and i love to learn python'''
print(multiline_string)

#other version to do the same thing
multiline_string = """i hope you guys will enjoy learning python"""
print(multiline_string)

#string concatenation means merging or connecting strings.
first_name = "Guido "
middle_name = "Van "
sur_name = "Rosem"
print("father of python: ",first_name + middle_name + sur_name)
full_name = first_name + middle_name + sur_name
print("father of python: " , full_name)
print(len(full_name))
print(len(first_name))

#escape sequence in strings: in python we have characters in string which is followed by a escape sequence, lets see some common escape sequence characters:

# \n: new line
# \t: tab means(8 spaces)
# \\\\: back slash
# \\': single quote(')
#\\": double quote(")

#lets us see their applications with examples.

print("i am enjoying the python challenge.\n thank you ") #line break
print("days\ttopics\texcersises")#adding tab space
print("day1\t5\t6") 
print("this is a backslash symbol(\\)")#to write a backslash
print("in every programming language it starts with \"hello, world!\"")#to write a double quote inside a double quote or inside a single quote

#string formatting
#this is old school where we use (% operator)
# %s :refers to any object with a string representation like numbers
# %d : for integers
# %f : floating point number
# %.<small> :number of digits.
# </small>f" :floating point number with fixed precision

#strings only
first_name = "albert"
last_name = "einestein"
field = "physics"
formated_string = "i am %s %s. i teach %s" %(first_name, last_name, field)
print(formated_string)

#strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "the area of circle with a radius %d is %.2f." %(radius, area)
print(formated_string)
python_libraries = ['django', 'flask', 'numpy', 'matplotlib', 'pandas']
formated_string = "the following are python libraries:%s " %(python_libraries)
print(formated_string)

#new style string formatting(str.format), introduced in python version 3

first_name = "albert"
last_name = "einestein"
subject = "physics"
formated_string = "i am {} {}. i teach {}".format(first_name,last_name, subject)
print(formated_string)
a = 4
b = 3
print("{} + {} + {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

#string and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "the area of a circle with a radius {} is {:.2f}.".format(radius, area) 
print(formated_string)

#string interpolation /f-strings(python 3.6+)
#another new string formatting is string interpolation , f-strings. strings start with f and we can inject the data in their corresponding positions.
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#python strings as sequences of character: python strings are sequence of characters and have same methods of access like lists and tuples. the easiest way to extract single character from strings, and individual members from any sequence is to unpack them into indvidual variables.
#unpacking characters
language = 'python'
a,b,c,d,e,f = language #unpacking sequence characters into variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# accessing character in strings by index
#in programming, indexing or counting starts from zero and the last letter of a string is the length of a string minus one.
language = "python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)

last_index = len(language) - 1
last_letter = language[last_index]
print(last_index)
print(last_letter)

#we can also do negative indexing starting backwards. -1 is the last index
language = "python"
last_letter = language[-1]
print(last_letter)
second_letter = language[-2]
print(second_letter)

# slicing python strings, in python we can slice strings into substrings
language = "Python"
first_three = language[0:3]
print(first_three)
#another way
last_three = language[-5:]
print(last_three)
last_three = language[5:]
print(last_three)
#revese the strings in python
greeting = "yoshua bengio"
print(greeting[::-1])

#string methods to format strings. lets see some example:

#capitalize():converts the string's first character into capital letter

ai_summit_2026 = "india, New delhi lead by president Modi jee"
print(ai_summit_2026.capitalize())
#count(): returns occurences of substring in string, count(substring, start-----end..) the start is the starting indexing for counting and end is the last index to count.

ai_summit_2026 = "there was huge investments from tech giants from Europe"
print(ai_summit_2026.count('a'))
print(ai_summit_2026.count('e', 1, 20))
print(ai_summit_2026.count("er"))
#endswith(): checks if a string ends with a specified ending

ai_summit_2026 = "india invited french president as the chief guest"
print(ai_summit_2026.endswith('what'))
#expandtabs(): we can use it to replace tab character with spaces, default tab size is 8.
ai_summit_2026 = "india\ninvited\tfrench\tpresident as the chief guest"
print(ai_summit_2026.expandtabs(12))
print(ai_summit_2026.expandtabs())

#fint():returns the indec of the first occurence of substring, if not found returns -1

ai_summit_2026 = "the central idea is about how to make ai safe and efficient"
print(ai_summit_2026.find('u'))
print(ai_summit_2026.find('ent'))
#rfind(): returns the index if the last occurence of a substring, if not found returns -1
ai_summit_2027 = "it will be held in geneva"
print(ai_summit_2027.rfind('va'))
#format(): format string into a nicer output.

first_name = "steve"
last_name = "jobs"
age = 35
job = "tech innovater"
country = "usa"
sentence = " i am {} {}, i am {} years.i am a {} based in {}.".format(first_name, last_name, age, job, country)
print(sentence)

raduis = 10
pi = 3.14
area = pi * radius ** 2
result = "the area of a circle with {} is {}".format(str(radius), str(area))
print(result)

#index(): returns the lowest index of a substring, additional aruments indicate starting  and ending index(default 0 and string length -1)if the substring is not found it will show a valueError






