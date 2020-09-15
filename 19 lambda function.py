func = lambda a,b:  print("The sum of two numbers is : ", (a+b))

type(func)

func(2, 10)

def new_func(list1):
    list2 = []
    
    for i in range(10):
        for j in range(5):
            result = i * j
            list2.append(result)
    return list2 + list1

print(new_func([10,20,30,40,50]))

# This whole new_func() can be done using one line code only,

new_func_advance = lambda mylist: [ x*y for x in range(10) for y in range(5)] + mylist

print(new_func_advance([10,20,30,40,50]))

# and it's done........... using only 1 line

def product10(a):    # created a function which takes input and multiplies it with 10
    return a * 10

r1 = range(10)       # created a range function of 10 elements

b = map(product10, r1)     # map the first function to range function

list(b)   # showing results using list, this will show a list of 0-9 numbers multiplied with 10

# now doing the same with a lambda function

b1 = map( (lambda a : a * 10 ) , r1 )   # mapping the lambda function with range function

list(b1)   # showing results using list, this will show a list of 0-9 numbers multiplied with 10

# now applying filter function

b2 = filter( (lambda a : a > 5 ) , r1 )   # filtering the lambda function with range function using condition

list(b2)