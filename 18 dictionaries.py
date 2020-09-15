# Dictionary in python 

# dictionaries in python are mutable datatypes, we can modify them
# dictionary contains a key and a corresponding value, keys should be unique

dict1 = {1 : "Shahzad" , 2 : "Rizwan" , 3 : "Kaleem"}

dict1
type(dict1) 

dict1[2]   # accessing the second element/key 2 of dict1

dict1[2] = 'Rizwan Ahmad'  # changing the value of key 2 in dict1

dict1   # values updated, key 2 value changed

dict1[4] = "Shahzad"  # adding a new key and a value

dict1  # dictionary may contain same values, but not same keys

del dict1[4]  # deleting the key 4 and its value from dict1

dict1   # key 4 and the value not present now

len(dict1)   # length of dict1 = 3

"Shahzad" in dict1   # to check if "Shahzad" is in dict1
# False, because the we can't check the values, we can check only keys

2 in dict1   # checking if key 2 is in dict1 or not?
# True


dict1.keys()   # returns a list of all the keys in a dictionary

dict1.values()   # returns a list of all the values in a dictionary

dict1.items()   # returns a list of tuples, each tuple containing pair of key and value



num = 10
type(num)

num = str(num)
num = int(num)

type(num)


str1 = "19897"

str1 = int(str1)

type(str1)




num_bin = bin(num)     # decimal to binary conversion

num_bin  # 0b1010 in binary


num_hex = hex(num)     # decimal to hexadecimal conversion

num_hex  # 0xa in hexadecimal


num = int(num_bin, 2)  # binary to decimal conversion, 2 must be included

num  # now num = 10 again


num1 = int(num_hex, 16)  # hezadecimal to decimal conversion, 16 must be included
num1 # now num1 = 10 



