x=[[10,20,30,],[1,2,3,4,5],[111,22,33,44]]
print(x)
print("Elements in rows")
for r in x:
    print(r)
print("Elements to be printed in matrix style")
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end='')
    print()