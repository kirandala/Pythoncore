'''ARRAYS IN PYTHON'''

''' Array will store only one kind of data type but list can store heterogenous data  type but  arays are very fast compared to
list and other collection datat type as while huge memory is taken then arry will take less space compared to list
Py array is not fixed in size so no need to specify no of elements we are going to store into array at beginning
array can grow or shrink during run time dynamically
Syntax: arrayname=array(type code, [elements])  
 type code    ctype
  b        -   signed integer              1
  B        -    unsigned interger           1
  i        -    signed interger             2
  I        -       unsigned interger        2
  l         -   signed integer              4
  L         -      Unsigned Interger        4
  f    -       floating point      4
  d         -       double floating point   8
  u            -    unicode character        2
  
   '''
# Array has to be imported before using it.
'''import array 
import array as ar  # we can use ar as the alias name while using the array keyword 
from array import *                                  '''
import array
# from array import *
a=array.array('i',[10,20,30,40])
print("elements of a are ")
for x in a:
    print(x)
print('the individual elements of a are ')
print(a[0])
print(a[1])
print(a[2])
print(a[3])

''' it is possible to create an array from another array '''

ar1=array.array('d',[10,30,50,70])
ar2=array.array(ar1.typecode,(n for n in ar1))
print('type code functionality for adding ar1 to ar2')
for x in ar2:
    print(x)


''' indexing and slicing on arrays is possible'''


'''Method availabe in array class'''
a4=array.array('i',[1,2,3,4,5,6])
print('original array of a4 is ',a4)
a4.append(7) # 7 will be added to array a4 at the end
b=a4.count(2) # Counts how many times 2 is available
print('a4 count of 2 is ',b)
print(' a4 after added 7 ',a4)
a4.index(3) # returs the position of 3
a4.reverse() # array will be reversed
a4.remove(5)  # 5 will be removed
a4.pop()
print('a4 after removing 5 and the last element using pop and reversing the array',a4)
print('a4 applying pop(0) index the removed item and returned item is:',a4.pop(0)) # it uses the index to remove the element
a4.insert(0,7) # 0 position add 7

''' a4.tofile(f) writes all elements to file f
  a4.tolist()  converts the array a4 to list
  a4.tostring() converts the array a4 to string 
  a4.fromstring(str) appends items from string to a4
  a4.fromlist(l)  appends items from list to a4
  a4.typecode - will represnt the type code character used to create the array a4
  a4.itemsize - will represent the size of tiems stored in the array(in bytes)
  
  '''
''' Program to enter the marks of student and print sum and average'''

print('Program to enter the marks of student and print sum and average 74 line')
str=input('enter the marks of students:').split(' ')
marks=[int(num) for num in str ]  # storing the marks into marks array
sum=0
for x in marks:
    print(x)
    sum+=x
print('total marks are',sum)
n=len(marks)
print('average of the students marks is ',sum/n)

''' Program to sort an array elements in ascending order using bubble sort
logic is each element of array a[0} will be compared with next element a[1] and if a[0] is bigger elements will swap
ie the place of a[0] will move to right "164"
'''
print('program to sort an array elements using bubble sort logic')
x=array.array('i',[])
print('how many elements do you want to add ?' ,end=' ')
n=int(input()) # accepts input into n
#run the loop to enter the n number of elements
for i in range(n):
    print('enter element:',end=' ')
    x.append(int(input()))  # adding the elements into array x
print('original array to be sorted is', x)
# applying bubble sort for the array x
flag=False # when swapping id done, flag becomes True
for i in range(n-1):
    for j in range(n-1-i): # j is for 1 element less than i
        if x[j]>x[j+1]:
            t=x[j] # swap j and j+1
            x[j]=x[j+1]
            x[j+1]=t
            flag=True  # swapping done hence making it true
        if flag== False:
            break  # come out of the inner loop
        else:
            flage=False  # assing initial value to flag
print('sorted array is ',x)


''' Program to search for the position of an element in an array using sequential search'''

'''program to search for postion using index() method'''



