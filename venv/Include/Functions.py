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
# def modify(lst):
#     ''' to add a new element into existing list'''
#     lst.append(10)
#     print(lst,id(lst))
# # call modify() and pass lst
# lst=[1,2,3,4]
# print(lst,id(lst))
# modify(lst)
# print(lst,id(lst))

'''progam to create a new object inside the funciton does not modify outside object'''
# def modify(lst):
#     '''to create a new list'''
#     lst=[1,2,3,4]
#     print(lst,id(lst))
# # calling modify fn
# lst=[10,20,30]
# modify(lst)
# print(lst,id(lst))

'''In fn we do have parameters ,these parameters will help to get values outside of the fn
the values we pass to parameters are arguments and there are :
Formal and actual arguments
the values or data we pass to the fn are actual arguments
Actual arguments:
positional arguments
keyword arguments
default arguments
variable length arguments
'''

''' :argument we add with respect to position , their position should exactly match with the postion and number of arguments
in the funtion call 
program to understand postional args'''

# def attach(s1,s2):
#     s3=s1+s2
#     print('total sring is ',s3)
# attach('new','York') # positional arguments when positions change the final string will have impact

'''keyword arguments are those that identify the paramenter by thier names
program to understand keyword arguments'''

# #keyword arguments demo
# def groc(item,price):
#     '''to display the given arguments'''
#     print('item=%s'%item)
#     print('price=%f'%price)
# # call groc() and pass 2 arguments
# groc(item='sugar',price=20) #key word arguments

''' Default arguments can mention some default value for the function parament in the definition if the value is not 
passed. Program to understand Default argument'''

# def groc1(item,price=40.00):
#     '''to display the given arguments'''
#     print('item=%s'%item)
#     print('price=%f'%price)
# # call groc() and pass 2 arguments
# groc1(item='sugar',price=20) # value is passed
# groc1(item='rice')#default argument price is not given so default value will be taken


'''Variable Length argument some times programmer doesnt know how many values a fn may require here we can use 
variable lenght argument will accept any number of values . these values will be stored in a tuple.
 Program to understand Variable length arguments'''
#
# def add(farg,*argv): #*args can take 0 or n values
#     '''to add numbers'''
#     print('formal arguments=',farg )
#     sum=0
#     for i in argv:
#         sum+=i
#         print('sum of all numbers=',(farg+sum))
#
# #calling the fun and passing values
# add(5,20)
# add(5,20,30,40,50)

''' keyword variable length argument is an argument that can accept any number of values provided in the format of keys 
 values. when key value variables are needed we can do by declaring ** before the argument'''

# def display(farg,**kwargs):
#     '''to display given values'''
#     print('formal arguments=',farg)
#     for x,y in kwargs.items():
#         print('key={} and value={}'.format(x,y))
# # calling funciton
# display(5,rollno=1)
# print()
# display(6,rollno=10,name='kiran')

'''Local and global variables
when we delcare a var inside fn, it becomes a local variable.- its scope is limited only to that fn
outside the fun that vari is not available'''
# def myfun():
#     a=1
#     a+=1
#     print(a)
# myfun()
# print(a) # we get always an error as a is not defined outside the function so args are only local to fun

# now lets declare a varialbe globally and try to access inside a fn
#global variala example
# a=1
# def myfun():
#     b=2 #this is local var
#     print('a=',a) #display global var
#     print('b=',b) #display local var
# myfun()
# print(a)# this will be displayed
# print(b)# this will not be displayed ,error


'''Global Keyword
sometimes local var and global var wil have same name,here fn ,by default ,refers to the local var and ignores the global var.
So, global var is not accessible inside the fn but outside ofit it is accesble.
program to understand this aura'''

#same name for local and global var
# a=1
# def myfun():
#     a=2
#     print('a=',a) # desplay local var
# myfun()
# print('a=',a)# display global var
# # for programer to use the global var inside the fun he can do by using global keyword
#
# a=1
# def myfun():
#     global a # this is global var
#     print('displaying global variable a=',a) # desplay global var
#     a = 2
#     print(' displaying local var a=', a)  # desplay local var
# myfun()
# print('a=',a)# display global var

''' global values once declared, local var cannot be used so here is a solution
the globals() fn will solve this problm. this is built in fn which returns a table of current global variables in the 
form of a dictionary.program to get a copy of global variable into a funtion and work with it'''

#same name for global and local variables
# a=1
# def myfun():
#     a=2
#     x=globals()['a'] #get global var into x
#     print('global var a =',x)
#     print('local var a=',a)
# myfun()
# print('global var a=',a)

''' passing group of elements to fun
program  function to accept a group of numbers and find their total average'''
# #Fn to find total and average
# def cal(lst):
#     ''' to find total and average'''
#     n=len(lst)
#     sum=0
#     for i in lst:
#         sum=sum+i
#         avg=sum/n
#     return sum,avg
# #take a group of int from keyboard
# print('enter numbers seperated by space:')
# lst=[int(x) for x in input().split()]
# #call calculate() and pass the list
# x,y=cal(lst)
# print('the sum is ',x)
# print('the average is',y)


'''Recursive Functions
fn calling itself is called recursive funtion
program to caluculate factorial using recursive function'''

# def fact(a):
#     '''to find the factorial using recursive funtion'''
#     if a==0:
#         return 1
#     else:
#         result=a*fact(a-1)
#         return result
# for i in range(1,8):
#     # calling fact() fn and finding fact by 1 to 7
#     print('factorial of {} is {}'.format(i,fact(i)))

'''Anonymous function or lambdas

fn without name is lambda and defined by lambda
syntax: lambda variablename: expression'''
# def square(x):
#     x*x
# #This program can be written in lambda function as
# lambda x: x*x
# f=lambda x: x*x # this fun will return the square of the given number
# print(f(5))

'''program to return sum of numbers using lambda fun'''
# f=lambda m,n:m+n
# sum=f(1,2)
#
# print(sum)

'''program to return the bigger number in two numbers'''

# f=lambda x,y: x if x>y else y
# print('enter the two numbers to compare')
# a,b=[int(n) for n in input().split()]
# print('bigger number is ',f(a,b))

'''filter() is useful to filter out the elements of a sequence depending on the result of the fun
Syntax:filter(funtion,sequence)
to test the element of a list 'lst' as:
filter(is_even,lst)
program to using filter out even numbers from a list
'''
#filter() function that returns even number from list
# def is_eve(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# print('enter the values of the list')
# lst=[int(x) for x in input().split()]
# lst1=list(filter(is_eve,lst))
# print(lst1)

# same program can be written in another way
#print('enter the values of list')
# lst=[int(x) for x in input().split()]
# lst1=list(filter(lambda x:(x%2==0),lst))
# print(lst1)

''' lambdas with map() fun
is similar to filter(0 but it acts on each element of the sequence and perhaps changes the elements
map(function,sequence)
program to find sqared of elements in a list'''
# def square(x):
#     return  x*x
# lst=[1,2,3,4,5]
# lst1=list(map(square,lst))
# print(lst1)
# # this program can also be written in a different way
# lst1=list(map(lambda x: x*x,lst))
# print(lst1)
#
# # it is possible to use map() on more than one list if it has samelength
# map(lambda x,y:x*y,lst1,lst2)

'''reduce() funtion
reduces a sequence of elements to a single value by processing the elements accordin to functions supplied
reduce(funtion,sequence)
'''
