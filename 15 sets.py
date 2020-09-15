# Sets  --- sets are mutable

# Difference between a set and a list is that sets dont have repeated values

list1 = [1 , 2 , 2 , 3 , 3 , 3 , 4 , 5]

set(list1)  # list is converted into a set but original list remains the same

set1 = set(list1)  # now converted list into set and saved to memory as well

type(set1)   # type of set1 is "set"

set2 = {1 , 2 , 3 , 3 , "a" , "b" , "b"}

set2

len(set1)
len(set2)

set1.add(6)

set1

set1.remove(6)

set1

set1.add(5)   # 5 already present. Sets dont have a duplicate value

set1


set1.intersection(set2)   # set1 intersection set2

set2.intersection(set1)  # set2 intersection set1

set1.difference(set2)   # set1 - set2

set1.union(set2)   # set1 union set2  - no repetition here too

set1.pop()   # deletes first element

set1

set1.clear()   # clears a set

set1   # now an empty set



# frozenset() - Frozen sets are immutable sets - 


list3 = [1 , 2 , 2 , 3 , 4 , 5]
list4 = [2 , 3 , 3 , 4 , 'a' , 'b']

set3 = frozenset(list3)
set4 = frozenset(list4)

set3
set4

type(set3)  # type frozenset

set3.intersection(set4)

set3.add(9)  # will give error, because frozensets cant be changed
