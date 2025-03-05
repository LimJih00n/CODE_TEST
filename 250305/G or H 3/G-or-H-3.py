n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
ans = float('-inf')
map_ = [0] *10001
for char,pos in zip(c,x):
    if char == "G":
        map_[pos] = 1
    if char == "H":
        map_[pos] = 2

for i in range(1,100001):
    sum_=0
    for j in range(i,i+k+1):
        if j>10000:
            break
        
        sum_ += map_[j]
    
    ans = max(ans,sum_)
print(ans)
        
