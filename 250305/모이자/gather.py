n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

min_dist = float('inf')

for i in range(n):
    sum_dist=0
    for j in range(n):
        if i==j:
            continue
        sum_dist += abs(i-j)*A[j]
    min_dist = min(sum_dist,min_dist)
print(min_dist)