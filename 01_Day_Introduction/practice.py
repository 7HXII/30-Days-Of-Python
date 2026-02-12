print("hello i am feeling great to learn python")
#basic operations
print(2+1) #add
print(4-2) #subtract
print(2*4)#multiply
print(2**4) #exponent
print(4/2)#division
print(6//4) #floor division/round off

#checking data types &
int = 10
print(type(int))

float = 2.3
print(type(float))

c = 1 + 3j
print(type(c))

string = "albert"
print(type(string))

list = [1, True, 3.4, "john"]
list.append ''
print(type(list))

tuple = (1, 2, 3, 5)
print(type(tuple))

set = {1, 2, 3, 4, 5}
print(type(set))
print(type({1, 2, 3, 4, 5})) #dual ways to check dtype
dict ={'salary':'20000'}
print(type(dict))
print(len(dict)) #check length