n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
what? nxn 격자에서 3x3격자를 옮기며 안에 있는 1의 개수 들세기
how?
r,c모두 탐색->check_coin함수:(r,c) 3x3만탐색하며 범위 넘아가면 return
1이면 count return
'''
ans = 0

def check_coin(r,c):
    count = 0
    for i in range(r,r+3):
        for j in range(c,c+3):
            if i>=n or j>=n:
                return -1
            if grid[i][j] == 1:
                count+=1
    return count 
for r in range(n):
    for c in range(n):
        ans = max(ans,check_coin(r,c))
print(ans)
