# String Variables

string1 = "Hello, how are you?"
string2 = 'I am fine, thank you!'
string3 = '''Why
so
sad'''
string4 = '''Don't \
be \
so \
sad '''

string1[1]
string2[5]
string3[-1]

len(string1)
len(string4)

string1.index("o")   # only shows the index of first "o"

string1.count("o")   # number of times "o" appears

string1.find("l")    # position of "l" in the string
string1.find("ow")   # position of "ow" in the string

string1.find("xyz")  # if required string not found, returns -1

string1.lower()   # converts to lower case, but the original string remains same

string1.upper()   # converts to upper case, but the original string remains same

string1.startswith("H")  # check if the string starts with "H"

string1.startswith("h")  # case sensitive. 

string1.endswith("?")    # check if the string ends with "?"


a = "   Hello World   "

a.strip()   # used to remove any white spaces at the beginning and at the end


b = "$$$Hello$World$$$"

b.strip("$") # used to remove any character from the beginning and from the end

b.replace("$", "") # used to replace any character with our desired character
                    # here it replaces "$" with "nothing"

c = "Microsoft Google Amazon Facebook Yahoo"

c.split(" ")  # split a string using a delimiter, here the delimiter we used is space
                # delimiter can be anything, split will split where delimiter appears
                # and it results in a List

"_".join(c)  # adds "_" (or anything) after every letter in a string


cisco = "cisco"
switch = " switch"
cisco + switch      # concatinate two strings

router = " router"
cisco + switch + router     # concatinate three strings

cisco*3         # makes 3 copies of the same string


"o" in cisco    # returns TRUE if finds "o" in cisco

"o" not in cisco    # "o" is not in cisco, it is incorrect, "o" is there so returns FALSE

"Cisco : %s, switch: %d, router: %f" % ("new" , 10 , 2)  # printing at different positions

print("Cisco : %s, switch: %d, router: %f" % ("new" , 10 , 2))  # same as above

"Cisco : %s, switch: %d, router: %.2f" % ("new" , 10 , 2)  # for 2 decimal points print

"Cisco : {}, switch: {}, router: {}".format("new" , 10 , 2) # works same as above, print as it is

# we ca use index of the value in the curly braces to change the position of values

"Cisco : {0}, switch: {1}, router: {2}".format("new" , 10 , 2) # values in same order

"Cisco : {2}, switch: {0}, router: {1}".format("new" , 10 , 2) # order changed

# one value can be used more than one time

"Cisco : {2}, switch: {0}, router: {2}".format("new" , 10 , 2)

# using f-strings

new1 = "HELLO"
new2 = 4
new3 = 10.45

f"print new1 = {new1}, new2 = {new2}, new3 = {new3}" # using f-strings we can directly use defined variables

f"print new1 = {new1.lower()}, new2 = {new2*3}, new3 = {new3}" # operation with variables

# String Slicing

string5 = "I live in Peshawar, Pakistan"

string5[10:18]  # this will slice from index 10 to 17

string5[10:]    # slice from index 10 to the end

string5[:9]     # slice from the beginning to the index 8

string5[:-1]    # from start till the end-1

string5[-8:]    # from index -8 to the end

string5[::2]    # from start to the end but select every second element

string5[::-1]   # to print the string in reverse order

string5[::-2]   # reverse order but gap of 2
