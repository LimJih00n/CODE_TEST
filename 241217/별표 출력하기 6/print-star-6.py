'''

3 0 7 
2 2 5
1 4 3

3 6 1

0 4 3 
1 2 5
2 0 7

n = 4
'''
n = int(input())
for i in range(n):
    for j in range(i*2):
        print(" ",end="")
    for j in range((n*2-1)-2*i,0,-1):
        print("* ",end="")
    print("")
for i in range(n-1): 
    for j in range(n-i*2):
        print(" ",end="")
    for j in range(i*2+3):
        print("* ",end="")
    print("")