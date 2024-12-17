n = int(input())

# n 0 n
# n-1 2 n-2
# n-2 4 n-3
# n-3 6 n-3

for i in range(n):
    for j in range(n-i):
        print("*",end="")
    for j in range(i*2):
        print(" ",end="")
    for j in range(n-i):
        print("*",end="")
    print()

