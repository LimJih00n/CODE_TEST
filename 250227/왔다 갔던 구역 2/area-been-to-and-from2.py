n = int(input())
x = []
dir = []
commands = []
for _ in range(n):
    xi, di = input().split()
    commands.append((xi,di))
    

# Please write your code here.
#  0 1 2 3
# 0~1~2~3~4
arr = [0] * 2001
cur = 0
for command in commands:
    x = int(command[0])
    if command[1] == "R":
        for idx in range(cur,cur+x):
            arr[idx+1000]+=1
        cur = cur+x
    elif command[1] == "L":
        for idx in range(cur-1,cur-x-1,-1):
            arr[idx+1000]+=1
        cur = cur-x

ans = [1 for n in arr if n>=2]
print(sum(ans))
