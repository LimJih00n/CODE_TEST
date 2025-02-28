x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

arr =[ [0]*2002 for i in range(2002)]

for x in range(x1[0]+1000,x2[0]+1000):
    for y in range(y1[0]+1000,y2[0]+1000):
        arr[x][y] = 2

for x in range(x1[1]+1000,x2[1]+1000):
    for y in range(y1[1]+1000,y2[1]+1000):
        arr[x][y] -= 1

p1x = float('inf')
p1y = float('inf')
p2x = float('-inf')
p2y = float('-inf')
area = 0
for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] ==2:
            area =1
            p1x = min(p1x,r)
            p2x = max(p2x,r)
            p1y = min(p1y,c)
            p2y = max(p2y,c)

if area == 0:
    print(0)
elif x1[0] == x1[1] and x2[0] == x2[1] and y1[0] == y1[1] and  y2[0] == y2[1]:
    print(0)
elif p1x==p2x and p1y==p2y:
    print(0)

else:
    print((abs(p1x-p2x)+1)*(abs(p1y-p2y)+1))
    
                