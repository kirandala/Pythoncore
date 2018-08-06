''' list,tuple,set will store group of individual objects but dictonary will hold key value pairs
create dictonary by d={}, or declare the values like d={100:'kiran',102:'raja',103:'maya'}
mutable
dynamic(increase or decrease size)
duplicates not allowed but values can have duplicates
index, slicing not available
order is not preserved
duplicate keys not allowed

program to enter details of students and their respective marks and display their result
'''

record={}
n=eval(input('Enter the number of students data to be entered'))
i=1
while i<=n:
    name=input('Enter the name of student')
    marks=input('Enter the marks ')
    record[name]=marks
    i=i+1
print("Name of student",'\t','Marks')
for x in record:
    print('\t',x,'\t\t\t',record[x])  #\t will give the space so that we get result as matrix

# To update a value in dict

l={1:'kiran',2:'hello',3:'shiva'}
print(l[2])
l[2]='baju'
print(l[2])
print(l)

