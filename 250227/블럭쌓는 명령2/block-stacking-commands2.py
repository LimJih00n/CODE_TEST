n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
blocks = [0]*(n+1)
for i,j in commands:
    for idx in range(i,j+1):
        blocks[idx] +=1
print(max(blocks))