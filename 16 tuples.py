# Tuples  -  tuples are immutable, we cannot change them after creating

tuple1 = ()   # creating empty tuple

type(tuple1)

tuple2 = (1 , 2 , 3 , 4 , 5 , 6 , 6  , 7 , "abc" , "a")   # for one element, we must put a comma after the first value

type(tuple2)   # now tuple2 is a tuple

# we can apply all slicing techniques to tuples

tuple2[3]

tuple2[4:6]

tuple2[::-1]   # reverse order

tuple2[::2]   # start to end with a step of 2



# Assigning the values of tuple to variables - mapping

tuple3 = ("Shahzad" , "Rizwan" , "Kaleem")

(var1 , var2 , var3) = tuple3    # assigning the values in tuple to variables
# number of values and variables must be the same
var1
var2
var3

# alternate method :

(a , b , c) = (1 , 2 , 3)   # another method of mapping or assigning values

a    # a = 1
b    # b = 2
c    # c = 3

len(tuple3)


tuple4 = (2 , 4 , 6)
tuple4 + (0 , 9 , 8 , 7)


tuple4 * 2

max(tuple4)
min(tuple4)

3 in tuple4   # will return False, because 3 is not present in tuple4

del tuple4   # for permanenetly deleting tuple, not just clearing

tuple4  # error, tuple4 is not present, because already deleted
