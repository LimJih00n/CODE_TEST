n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
arr = [[0]*202 for i in range(202)]
#
for point in points:
    for x in range(point[0]+100,point[0]+108):
        for y in range(point[1]+100,point[1]+108):
            arr[x][y] = 1
print(sum([sum(n) for n in arr]))
