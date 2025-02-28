x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.

arr =[ [0]*2002 for i in range(2002)]

for x in range(x1[0]+1000,x2[0]+1000):
    for y in range(y1[0]+1000,y2[0]+1000):
        arr[x][y] = 2

for x in range(x1[1]+1001,x2[1]+1000):
    for y in range(y1[1]+1001,y2[1]+1000):
        arr[x][y] -= 1

ans = [1 for row in arr for v in row if v>=1]
if x1[0] == x1[1] and x2[0] == x2[1] and y1[0] == y1[1] and  y2[0] == y2[1]:
    print(0)
else:
    print(sum(ans))
    
                