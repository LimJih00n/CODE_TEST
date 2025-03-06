n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


# Please write your code here.
'''
what?: check point 하나를 제외하고 합쳐지는 거리의 최소를 구하기. 
how?: check point 하나씩 제외하면서 모든 거리를 구하고 최소 거리를 찾기
모든 check point를 순서대로 방문함
-> for문 탐색. 제외하고 또 탐색 (이중 반복문 필요)
1번과 n번은 못 건너뛴다.
'''
ans = float('inf')

for i in range(1,n-1):
    dis_po = points[:]
    del dis_po[i]
    x = [p[0] for p in dis_po]
    y = [p[1] for p in dis_po]
    dist = 0
    for j in range(1,n-1):
        dist += (abs(x[j]-x[j-1]) + abs(y[j]-y[j-1]))
    ans = min(ans,dist)
print(ans)