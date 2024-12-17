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
# 6 => 4 3 2 1 0
# 8이여야함 
#  2 1 0
#4 4 2 0
#5 6 4 2 0
#  0 1 2 3 4
#6 8 6 4 2 0
#     5 4 3 2 1 0
#7 10 8 6 4 2 0
for i in range(n-2,-1,-1): # 2 1 0 n = 4
    for j in range(i*2): #4 2 0
        print(" ",end="")
    for j in range((n-i-1)*2+1): # 3 5 7 => 2*i+1 (n-i)*2+1
        print("* ",end="")
    print("")