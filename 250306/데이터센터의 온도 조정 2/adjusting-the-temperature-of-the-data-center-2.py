N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
'''
A의 경우: Ta > T-> C
B의 경우: Ta <= T <= Tb -> G
C의 경우:  T > Tb-> H

장비들 마다 온도 범위에 따라 할 수 있는 작업량이 다르다.
가장 높은 값을 구하는 것이 목표이다.

1. 온도를 조절해가며 -> 온도의 최대 범위안에서
2. 각 기계들의 조간에 따라 능률량을 더한 후 -> max 구하기
'''
def compute_work(T):
    tot_work = 0
    for Ta,Tb in ranges:
        if Ta >T:
            tot_work += C 
        if Ta<=T<Tb:
            tot_work +=G
        if T>Tb:
            tot_work +=H
    return tot_work
ans = 0
for i in range(0,1001):
    ans = max(compute_work(i),ans)
print(ans)
    
        