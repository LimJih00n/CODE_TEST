n = int(input())

for i in range(n):
    for j in range(i*2):
        print(" ",end="") # j가 이미 i 에 따라 변하며 반복한다! 주의주의
    for j in range(n*2-1-(i*2),0,-1):
        print("* ",end="")
    print()
# n =2
#0 3
#1 1

# n = 3
# 0 5
# 1 3
# 3 1

# n = 4
0# 0 7
1# 2 5
2# 4 3
3# 6 1