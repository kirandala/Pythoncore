# \n is for new line \t is for tab spacing

# OUTPUT OPERATIONS
# print() function is used to display the output , howerver it can be used in different formats to print

print("hi this is {} please do not {}".format('name','talk'))

print("the first one is {0} and the thrid one is {2} and second one is {1}".format('one','two','three'))

# the indexing will b`e done as a tuple and hence the indexing should start with 0 .

# we also can print muliple variable in py but in java it cant so comma will work
a,b=1,2
print('values of a,b are',a,b)

'FORMATTED STRINGS     we can use %i -integer %d-floating point number %s for string literal and for single character %c'
# x=10
# print('integer value %i'%x)

# y=10.7868974
# print('Floating value is %f'%y)
# print('floating value with two decimal points is {:0.2f}'.format(y))   # restrict decimal integer to 2 digits

z='hello python'
print('String literal is %s'%z)

#program to find input two integers and find sum

# num1=eval(input("enter the value of num1 "))
# num2=eval(input('enter the value of num2'))
# print('the sum of {} and {} is {}'.format(num1,num2,num1+num2))

# convert the value  hexadecimal, octa and binary to binary system
# str=input("value of str")
# hexa=int(str,16) # converting to hexa with step number 16
#
# str1=input(" enter value of str1")
# octa=int(str1,8) # octa means to base 8
#
# str2=input(" enter value of str2")
# binary =int(str2,2) # value with base 2
# print("convertions of to binary for {} {} {} are {} {} {}".format(str,str1,str2,hexa,octa,binary))


# we also can access variables from a tuple list dict or set data.

# TAGS and place holders

tag='hello kiran'
mape='it will be second part of string'
sentence='<{0}>{1}</{0}>'.format(tag,mape)
print(sentence)


per={'name':'kiran', 'age':25,'place':'blr'} # this is dict

print('hello my name is {} and my age is {} belong to {}'.format(per['name'],per['age'],per['place']))
# this is one way where we give the dictonary values at the end {} are place holders
# using this we are adding the values in sequence for placeholder to pick


print('hello my name is {0[name]} and my age is {0[age]} belong to {0[place]}'.format(per))

''' Now, we can directly place the variable at the placeholer and name dict at the format 
but make a note that the index should be zero at place holder'''

# let us acces variable form the list type
l=['kiran',26]
print('hello this is {0[0]} and my age is {0[1]}'.format(l))
''' As we are dealing with list data we can access date with the index so the index will be given at the place holder'''




'''INPUT OPERATIONS'''

# input statement for entering two numbers in same line using split statement.
# m,n=[int(x) for x in input('enter the max number and min number').split() ]
# print(m,n)

a,b,c,d=[int(x) for x in input("enter the values of a,b,c,d").split()]
print(a,b,c,d,sep='\n')