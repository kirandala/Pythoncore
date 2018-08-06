#IMPORTING MATH MODULE
import math
# from math import factorial # this will import only factorial function from math module

# import math as m # this will give an ease to code math module will be nameed as m and m can be taken to perform any action


# n=eval(input("enter the number to find factorial"))
# print("Factorial of {} using factorial fucntiion from math module is {}".format(n,math.factorial(n)))

#program to find factorial of a number using recursion function

def fact(n):
    if n==0:
        return 1
    else:
        result= n*fact(n-1) # factorial function will again be called here untill n==0 calling same fn again
        return  result
n=5
m=fact(n)
print("factorisl of {} using recursion fuction is  {}".format(n,m))\


a,b=20,200

# funtions in math module
print("The ceil value of 10.7 is ",math.ceil(10.6)) #prints the next highest integer
print("The floor value of 10.7 is ",math.floor(10.7))# prints the previous lowest integer
print("the cos 90 is ",math.cos(90))
print("convert 180 from radians to degrees",math.degrees(180))
print("convert 180 from degrees to radians",math.radians(180))
print("prints exponetial value of 0.5",math.exp(0.5))
print("fsum will retun the exact sum of floating point values",math.fsum([60.233,23.908])) #will take only one argument
print("fmod will return the value for floating point values",math.fmod(120,10.5))
print("log10(x) will return the logaritm value for base 10",math.log(1,10))
print("absolute value of x is ",math.fabs(10.2))
print("square root of the 4 is ",math.sqrt(16))
print("pow is use to find the power of x to y",math.pow(2,3))
print("gcd will find the gcd of x,y ", math.gcd(10,100))
print("the real of the int x is truncated and returned",math.trunc(15.89897))
print('prints bool value if x is positve or negative infinity isinf(x)')
num=float('inf')# num is a float number that indicated infinity
math.isinf(num)
print("NAN not a number, so returns true if num is not a number else return false",math.isnan(10))

''' python support the contants like pi , e,inf,nan inf is floating point positive entity and nan is floating point not a number.
pi can be used to find the area of circle etc
'''
