# Ranges - range()

range1 = range(10)   # a range from 0 to 10, but not including 10

type(range1)   # type = range

range1   # this will only print starting and last element of range

print(range1)   # this will also print same, starting and last element

list(range1)   # this will list the whole range from start to the end

list(range1[2:5])   # slicing the range datatype, using list to show all elements

list(range1[3:9:2])  # slicing the range datatype with a step of 2

list(range1)[3:9:2]   # another way to slice, this will return same as the last command

list(range(20))  # we can still use range function without creating it first

len(range1)   # length is 10, 0 to 9

10 in range1   # False, because 10 is last element and is not included

7 not in range1   # False, because 7 is in range1

range1[3]   # element at index 3

range1.index(5)   # returns the index of 5






