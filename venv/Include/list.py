''' list and tuple concepts with important points '''

'''Array and list are same but list can store heterogenous data while array will accept only homogenious data'''
lst=[10,20,'gopal','m',40]
# empty list can be created by []
print(lst)

'''program to create a list using range() function'''

lst=range(10)
for i in lst:
    print(i,end=' ')
print()# thorw cursor to next line

#create a list from integer from 5 to 8
lst1=range(5,10)
for i in lst1:
    print(i,end=' ')
print()

#create a list with odd numbers from 5 to 9
lst2=range(5,9,2) # giving step number 2
for x in lst2:
    print(x,end=' ')

