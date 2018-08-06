''' COntrol statements are
if, if else, if elif, else suite,for , while, pass, return, assert ,break, continoue
prgm with same indentation is suite '''

'''program to find if the entered number is even or odd'''
# num1=eval(input('enter the number'))
# if num1%2==0:
#     print("number is even")
# else:
#     print('number is odd')

'''program to print the entered digit to word'''
# num2=eval(input('enter any digit from 0 to 5'))
# if num2==1:
#     print('one')
# elif num2==2:
#     print('Two')
# elif num2==3:
#     print('three')
# elif num2==4:
#     print('four')
# elif num2==5:
#     print('five')
# else:
#     print('Zero')

'''Proram to print the prime numbers for given maximum number '''

# num3=eval(input('Enter the maximum number to print prime number'))
# for num in range(2,num3+1):
#     for i in range(2,num):
#         if (num%i)==0:
#             break # break statement will take control out of loop and this will work when num3 is not prime numbeelse:
#     else:
#         print(num)

'''program to print the prime numbers between the range'''
# m,n=int(input('enter the maximum and minimum number to print prime numbers with space between two numbers').split())

# m,n=[int(x) for x in input('enter the max number and min number').split() ]
# for x in range(m,n+1):
#     if x>1:
#         for i in range(2,x):
#             if(x%i)==0:
#                 break
#         else:
#             print(x)

'''program to print the n number of fibinoci series '''
fib=eval(input('enter the range of fibinocci series'))
f=0
f1=1