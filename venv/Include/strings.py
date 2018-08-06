''' Strings and characters'''
s='hello'
s1="Hello "
s2=''' hello this is good
one  to present '''

s3='Hi kiran said "hello how are you" and am fine'

''' There are escape characters in python which can help to display outputs in different way
\t - tabspace
\n new line
\b- backspace
\v - vertical tabspace
\\- add single \
\a - bell or alert
\r - enter button


'''
''' program to access each element of a string in forward and reverse order also'''

# str1=input('enter the string')
# n=len(str1)
# i=0
# while i<n:
#     print(str1[i],end=' ')
#     i+=1
# print() # empty line
# i=-1
# while i>=-n:   # accessing elements in reverse order
#     print(str1[i],end=' ')
#     i-=1
# print()
# i-=1
# while i>=n:
#     print(str1[-i],end=' ')
#     i+=1


'''Program to access the characters of string using for loop'''
# str2=input('Enter a string')
# n=len(str2)
# for i in range(0,n):
#     print(str2[i],end=' ')# end to print in straight line
# print()
# # the above program can also be written usnig slicing operator as
#
# for i in str2:
#     print(i,end=' ')
# print()
# for i in str2[::-1]:
#     print(i,end=' ')

''' slicing the strings 

stringname[start:stop:stepsize]
str[::] - access from 0 th nth index
str[::2] - entire sting with setp no 2
str[2:] - starting form 2 to last index
str[:3] - starting from 0 to 3 index
str[-4:-1] - starting from -4 to -1 in reverse order
str[-6::] - access from -6 to end of the string in reverse order
str*3 - repeat str for three times (string repeation operator)
we also have membership operator for strings which will return True or False value

in and not in
example: string in string2 or sting not in string 2

'''
''' finding substring can be done in many ways
these wil return the 1st occurance of the substring
find()- returns -1 if substring not found 
rfind()- to find from right to left
index()- will retun valueError if not found
rindex() - to find from right to left
'''
'''program to find if sub string exits in main string or not'''

# str=input('enter the main string')
# sub=input('enter the sub string')
# if sub in str:
#     print('substring is availabe ')
# else:
#     print('sub sting in no availabe in main string')
#
# #same program can be written in another manner
#
# if sub not in str:
#     print('sub string not avaialbe in main string')
# else:
#     print('sub string is availabe here also')


'''' Program to find the first occurance of the substring'''

# str=input('enter the main string')
# sub=input('enter the sub string')
#
# # find the position of sub in str
# #search from 0 to nth index
# n=str.find(sub,0,len(str))   # this iwll return -1 if not available
#
# if n==-1:
#     print("string not available")
# else:
#     print('string availabe in',n+1)
#




''' program to find first occurance of the sub string in main string using index() '''

# str=input('enter the main string')
# sub=input('enter the sub string')
# #find the position of sub in str
# #search form 0 to nth index
# try:
#     n=str.index(sub,0,len(str))
# except.ValueError:
#     print('string not available')
# else:
#     print('string availabe in ',n+1)


'''Program to display all positions of a substring
 Note:find() and inde() will display only first occurance'''

str=input('enter the main string')
sub=input('enter the sub string')

i=0
flag=False
n=len(str)
while True:

'''space is also considered as character in string'''
'''program to remove spaces from string'''
# name='         kiran kumar     '
# print(name)# original name
# print(name.rstrip()) # remove the space on right side
# print(name.lstrip()) # remove the space on left side
# print(name.strip())  # remove the entire space
#
#






