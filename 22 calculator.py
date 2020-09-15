# A scientific calculator

import math

print("\nScientific Calaulator\n\n")


use = "y"


while( use == "y"):
    
    print("Please select a number corresponding to your desired calculation to perform it!\n\n")
    print("1  - Addition\n2  - Subtraction\n3  - Multiplication\n4  - Division\n5  - Modulo\n6  - Raising to a power\n7  - Square root\n8  - Logarithm\n9  - Sine\n10 - Cosine\n11 - Tangent\n")
           
    choice = float(input("\nEnter the number of your desired calculation : "))
    
    if( choice == 1 ):
        var1 = float(input("Please enter the first number for addition : "))
        var2 = float(input("Please enter the second number for addition : "))
        print("\nThe addition of these two numbers is : " , (var1 + var2))
        
    elif( choice == 2 ):
        var1 = float(input("Please enter the first number for subtraction : "))
        var2 = float(input("Please enter the second number for subtraction : "))
        print("\nThe subtraction of these two numbers is : " , (var1 - var2))
        
    elif( choice == 3 ):
        var1 = float(input("Please enter the first number for multiplication : "))
        var2 = float(input("Please enter the second number for multiplication : "))
        print("\nThe multiplication of these two numbers is : " , (var1 * var2))
        
    elif( choice == 4 ):
        var1 = float(input("Please enter the first number for division : "))
        var2 = float(input("Please enter the second number for division : "))
        print("\nThe division of these two numbers is : " , (var1 / var2))
        
    elif( choice == 5 ):
        var1 = float(input("Please enter the first number for modulo : "))
        var2 = float(input("Please enter the second number for modulo : "))
        print("\nThe modulo of these two numbers is : " , (var1 % var2))
        
    elif( choice == 6 ):
        var1 = float(input("Please enter the base : "))
        var2 = float(input("Please enter the power : "))
        print("\nThe answer is : " , (pow(var1 , var2)))
        
    elif( choice == 7 ):
        var1 = float(input("Please enter a number to get square root : "))
        print("\nThe square root of the given number is : " , (math.sqrt(var1)))
        
    elif( choice == 8 ):
        var1 = float(input("Please enter the number for calculating Logarithm to base 2 : "))
        print("\nThe logarithm of the given number is : " , (math.log(var1 , 2)))
        
    elif( choice == 9 ):
        var1 = float(input("Please enter the value (in degrees) to calculate the sine function : "))
        print("\nThe sine of the given value is " , (math.sin(math.radians(var1))))
        
    elif( choice == 10 ):
        var1 = float(input("Please enter the value (in degrees) to calculate the cosine function : "))
        print("\nThe cosine of the given value is " , (math.cos(math.radians(var1))))
        
    elif( choice == 11 ):
        var1 = float(input("Please enter the value (in degrees) to calculate the tangent function : "))
        print("\nThe tangent of the given value is " , (math.tan(math.radians(var1))))
        
    else:
        print("\n\nIncorrect option, please try again!\n\n")
    
    
    use = input("\nDo you want to use this calculator again? (y/n) : ")
    
    if( use == "y"):
        continue
    else:
        break
    