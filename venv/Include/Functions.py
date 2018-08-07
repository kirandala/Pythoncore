''' a group of statments that are intended to perform a specific task '''

''' For any part of program which needs to be executed again and again we can use function 
function and method are smae but when a function is written inside a class it is method and it can be called using 
object.methoname()
classname.methodname()
python defining a function using keyword def:
funtion body called suite nad first string is docstring
we can return the results from a funciton using return statements 
'''

'''program to add subtract and multipy using function 
Note: we can return multiple values in python functions'''
# def res(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     return c,d,e
#
# x=res(20,10)
# print('the result of the funtions is ')
# for i in x:
#     print(i,end=' ')

'''program to if given number is even or odd using function'''

# def evenodd(a):
#     if a%2==0:
#         print('the value is even')
#     else:
#         print('the value is odd')
#
# evenodd(2)
# evenodd(12125)

'''program to find the factorial of number using function'''

# def fact(a):
#     '''to find the factorial of a number'''
#     prod=1
#     while a>=1:
#         prod*=a
#         a=a-1
#     return prod
# print('the factorial of 5 is',fact(5))
# print('the factorial of 9 is',fact(9))
# print('factorial of first 9 numbers is ')
# for i in range(9):
#     print('the factorial of {} is {}'.format(i,fact(i)))

'''program to find the first n prime numbers using fucntions'''

# def prime(n):
#     ''' To find if the number is prime number or not'''
#     x=1
#
#     for i in range(2,n):
#         if n%i==0:
#             print(" it is not a prime number ")
#             x=0
#             break
#         else:
#             x = 1
#             print(' number is prime number')

# print(prime(30))

'''program to generate prime numbers using functions'''
# def prime(n):
#     ''' To find if the number is prime number or not'''
#     x=1
#     for i in range(2,n):
#         if n%i==0:
#             x=0 #this will be 0 if x is not prime
#             break
#         else:
#             x = 1
#     return x
# num=int(input('how many primes do you want ? '))
# i=2 # initial value of prime number must be 2
# c=1 # this will count the number of prime numbers
# while True: # repeat for ever
#     if prime(i): # if i is prime then display
#         print(i)
#         c+=1 # increase the counter
#     i+=1    # the next number to test
#     if c>num: # if count exceeds  the num
#         break # come out of the loop

''' when we create a fn python intrepeter automatically creates a object , as fun are objects we can pass fucntions to 
antoher functions just like we pass objet to a fun . 
its possible to return funtion from another fun 
note:
its possible to assing a fun to a variable
its possible to define one fun inside another fun
its possible that a fun can retun another fun
its possible to pass a fun as parameter to another function
'''

'''Program to understand how to assign a fun to a variable'''
# assign a fun to a variable
# def display(str):
#     return 'hai'+str
# # assingning function to variable x
# x=display('\tkiran')
# print(x)

'''Program to define function inside another function'''

# def display(str):
#     def message():
#         return ' how are you?'
#     result = str + message()
#     return result
# print(display('hello'))

'''program to know how to pass a funtion as parameter to another fun'''
#
# def display(str):
#     return str+'  kiran '
# def message():
#     return 'how are you'
# # call display() fn and pass message() fn
# print(display(message()))

'''program to know how a function can return another function'''
# to be observed properly

# def display():
#     def message():
#         return 'how are you'
#     return message   # we are returning another fn message
# #call display() fn and it reutns mesage() fn
# fun = display()
# print(fun())   # we are returing another function

''' program to pass list and modify it'''
def modify(lst):
    ''' to add a new element into existing list'''
    lst.append(10)
    print(lst,id(lst))
# call modify() and pass lst
lst=[1,2,3,4]
modify(lst)
print(lst,id(lst))
