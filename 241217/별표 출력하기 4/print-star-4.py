n = int(input())
for i in range(n,1,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("*")
for i in range(2,n+1):
    for j in range(i):
        print("*",end=" ")
    print()