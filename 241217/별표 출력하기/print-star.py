n = int(input())

for i in range(1,n):
    for j in range(i):
        print("*",end=" ")
    print()
print("* "*n)
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()