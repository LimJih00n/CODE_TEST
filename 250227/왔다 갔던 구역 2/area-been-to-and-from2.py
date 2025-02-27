n = int(input())
x = []
dir = []
commands = []
for _ in range(n):
    xi, di = input().split()
    commands.append((xi,di))
    

# Please write your code here.
arr = [0] * 2001
cur = 0
for command in commands:
    x = int(command[0])
    if command[1] == "R":
        for idx in range(cur,cur+x):
            arr[idx+1000]+=1
        cur = cur+x+1
    elif command[1] == "L":
        for idx in range(cur,cur-x,-1):
            arr[idx+1000]+=1
        cur = cur-x-1

ans = [1 for n in arr if n>=2]
print(sum(ans))
