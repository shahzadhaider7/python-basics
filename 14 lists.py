# --- Lista are mutable, they can be changed  ---

list1 = []   # an empty list
type(list1)

list1 = ["Hello" , "I live in Peshawar" , 25000 , 7000000 , 10.9 , -9767857]

len(list1)

list1[1]   # access the second element of list

list1[-1]   # access the last element of list

list1[3]

list1[::2]

list2 = [23 , 343 , 3536 , -243543 , -998]

max(list2)
min(list2)

list1.append(10)  # add an element to the list

print(list1)

del list1[-1]    # delete an element from the list

list1

list1.pop(-1)    # another way to delete an element from the list

list1

list1.remove("Hello")   # third way to delete an element from the list

list1

list1.insert(0, "Hello")   # to add an element at an index in a list

list1

list1.extend(list2)   # to add a list to another list

list1

list1.index(23)   # returns the index of an element

list1.append("Hello")   # adding second hello to the list

list1.count("Hello")   # returns the count of the given element

list2

list2.sort()   # to sort a list in ascending order

list2

list2.reverse()   # to sort a list in descending order or reverse a list

list2

print(list2)

sorted(list2)   # this will create another list and sort it, the original list will remain the same

sorted(list2 , reverse = True)   # original list remains the same

list2


list1 + list2   # adding two lists

list2 * 3   # multipling 3 to list2, original list remains the same

list2


# Slicing Lists

list3 = [1 , 1 , 2 , 3 , 'a' , "b" , "c d"]
list3

list3[2:]   # from index 2 till the index

list3[3:5]  # from index 3 to 5

list3[-1]   # last element of the list

list3[-6:-1]  # from index -6 till the end, but not the last element

list3[-6:]    # from index -6 till the end including the last element

list3[2:6:2]  # from index 2 to index 6, with a step of 2

list3[::]     # from start till the end

list3[::-1]   # reverse the list, from the end to the start
