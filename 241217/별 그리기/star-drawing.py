n = int(input())

'''
0 2 1 
1 1 3
2 0 5

0 1 3
1 2 1
'''

for i in range(n): # 0  1 2
    for j in range(n-i-1): # 3 => 3번
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i*2):
        print("*",end="")
    
    print()
    