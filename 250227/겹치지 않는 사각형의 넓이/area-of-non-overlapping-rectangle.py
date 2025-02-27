x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
arr = [[0]*2000 for i in range(2000)]
for y in range(y1[0],y2[0]):
    for x in range(x1[0],x2[0]):
        arr[y][x] = 1
for y in range(y1[1],y2[1]):
    for x in range(x1[1],x2[1]):
        arr[y][x] = 1
for y in range(y1[2],y2[2]):
    for x in range(x1[2],x2[2]):
        if arr[y][x]:
            arr[y][x] = 0
print(sum([sum(row) for row in arr]))