#list: collection of data types, ordered and modifiable. it can be empty or it can contain different data type items.

#syntax
lst = list()

#list can be created in two ways.
#syntax
lst = list()
#1 built-in 

empty_list = list()#empty 
list
print(len(empty_list))

#using square brakcets:[]

lst = [1, 2, 3]

fruits = ['banana', 'orange', 'mango', 'lemon']

#list of fruits

alpha = ['a', 'b', 'c', 'd']
#list of alphabets

cars = ['bmw','rollsroyce','land-rover']
#list of cars

phone = ['nokia', 'samsung', 'iphone']

#list of phones
print("alphabets: ", alpha)
print("cars: ", cars)

#list can contain different data types
#list can be accessed using their index, the list index starts from 0.


cars = ['bmw','rollsroyce','land-rover']
first_car = cars[0]
print("car: ",first_car)

last_index = len(cars) -1 
last_car = len(cars[last_index])
print(last_car)

#unpacking list items

lst = ['book','chair','bottle','phone','cup']
first_item, second_item, third_item, *rest = lst
print(first_item)
print("item: ", second_item)
print(rest)

first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['Germany', 'France','england','india','bhutan','bangladesh','afganistan','Norway','Estonia']
gr, fr, uk, *asia, nr, es = countries
print(gr) 
print(fr)
print(uk)
print(asia)
print(nr)
print(es)
all_countries = countries[0:4]
print(all_countries)

#checking items in list using #in# operator

phones = ['nokia', 'samsung', 'iphone', 'vivo']
present = 'vivo' in phones
print(present)
present = 'vodaphone' in phones
print(present)

#adding items to list: we use a keyword called #append()# at the end of the ending list.

#syntax
lst = list()
lst.append('item')


phones = ['nokia', 'samsung', 'iphone', 'vivo']
phones.append('vodaphone')
print(phones)

#inserting items into list

#we use *insert()* method to insert a single item at a specific index in a list. the previous itemms are shifted to the right and it takes two arguments: index number and a item to insert.

#syntax
lst =['item1', 'item2']
# lst.insert(index, item)

phones = ['nokia', 'samsung', 'oppo', 'vivo', 'motorola']
phones.insert(2, 'google')
print(phones)

#removing items from a list
#remove method removes the specific item from a list.

#syntax 
lst = ['item1', 'item2']
#lst.remove(item)

animals = ['cat', 'dog', 'cow', 'hen']
animals.remove('hen')
print(animals)

#remmoving items using pop: the *pop()* method removes the sepcified index, or the last item if index is not specified

animals = ['cat', 'dog', 'cow', 'hen']
animals.pop(1)
print(animals)

#removing items using Del: the *del* keyword removes the specified index and it can also be used to delete items

senses = ['eye', 'nose', 'ear', 'tongue', 'skin']
del senses[2]
print(senses)

del senses[1:3]
#clearing list items: the *clear()* method empties the list.

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits) 

#copying a list: we can use #copy# to copy a list , it is used when we dont want to alter the original list.

fruits = ['watermelon', 'kiwi', 'leechi', 'avacado']

fruits_copy = fruits.copy()
print(fruits_copy)

#joining list: there are many ways to join lists in python.
#1 plus operator(+)

prime_numbers = [2, 3, 5, 7, 9, 11]
natural_numbers = [1, 2, 3, 4, 5]
whole_numbers = [0, 1, 2, 3, 4, 5]
numbers = prime_numbers + natural_numbers + whole_numbers
print(numbers)

boy = ['jack', 'tom','jimmy']
girl = ['marry','hania', 'lisa']
boy_and_girl = boy + girl
print(boy_and_girl)

#joining using extend metthod: the *extend()* method can add list in a list.

num1 = [0, 1, 2, 3, 4, 5]
num2 = [6, 7, 8, 9, 10]
num1.extend(num2)
print("numbers: ", num1)

week = ['mon', 'tue', 'wed', 'thur', 'fri']
month = ['jan', 'feb', 'mar', 'april']
week.extend(month)
print(" week: ", week)

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5,]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)

print("inetegers: ", negative_numbers)

#counting items in a list: the *count()* method returns the number if items appears in a list

lst = ['one', 'two','three', 'four', 'five','six']
print(lst.count('four'))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))

#finding index of an item:*index()* method retns the index of an item in the list.

fruits = ['banana', 'plum', 'peach', 'pear', 'mango']
print(fruits.index('mango'))

#*reverse()* method reverses the order of a list

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)



height = ['150', '160', '170', '140']
height.reverse()
print(height)


#sort modifies the original list 

cars = ['kia', 'hyundai','ms',]

cars.sort()
print(cars)

cars.sort()
cars.sort(reverse = True)
print(cars)

#sorted: returns the ordered the list without modifying the original list

fruits = ['banana', 'apple','orange','pineapple']
print(sorted(fruits))




