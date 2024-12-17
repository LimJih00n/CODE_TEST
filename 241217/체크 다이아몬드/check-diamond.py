'''
i v *
0 3 1
1 2 2
2 1 3
3 0 4

3 1 3
2 2 2
1 3 1

'''
n = int(input())

for i in range(n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()