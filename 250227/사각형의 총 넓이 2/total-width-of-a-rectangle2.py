n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
arr =[[0]*201 for _ in range(201)]
for r in range(y1[0],y2[0]):
    for c in range(x1[0],x2[0]):
        arr[r+100][c+100]=1
for r in range(y1[1],y2[1]):
    for c in range(x1[1],x2[1]):
        arr[r+100][c+100]=1
tot = sum([sum(n) for n in arr])
print(tot)
