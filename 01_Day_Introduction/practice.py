print("hello i am feeling great to learn python")
#basic operations
print(2+1) #add
print(4-2) #subtract
print(2*4)#multiply
print(2**4) #exponent
print(4/2)#division
print(6//4) #floor division/round off
print(4<6)#less than
print(4>2)#greater than
print(8==8)#equal
print(5!=3)#not equal
print(6<=4)#less than or equal 
print(5>=9)#greater than or equal


#assignment operators
x = 6# use variable
x /= 2 #x = x / 2
print(x)

y = 6 # use variable
y %= 5#y = y % 5
print(y)

z = 5 #use variable
z **= 3#z = z ** 3
print(z)

#checking data types 
int = 10
print(type(int))

float = 2.3
print(type(float))

c = 1 + 3j
print(type(c))

string = "albert"
print(type(string))

list = [1, True, 3.4, "john"]
print(type(list))

tuple = (1, 2, 3, 5)
print(type(tuple))

set = {1, 2, 3, 4, 5}
print(type(set))
print(type({1, 2, 3, 4, 5})) #dual ways to check dtype
dict ={'salary':'20000'}
print(type(dict))
print(len(dict)) #check length

#list operations
list = [1, 2, 3, 4, 5]
#indexing
print(list[0])#first element
print(list[-1])#last element
#slicing[start:stop:step]
print(list[::2])#[1, 3, 5]
print(list[::-1])#reverse list
print(list[1:2:2])
list = [1, 2, 3, 4, 5]
list.append(6)
print(list)
list.insert(2,10)#(index,value)
print(list)
list.remove(4)
print(list)#removes the value
list.sort(reverse = True)
print(list)#reverse list
list.clear()#clear list
print(list)