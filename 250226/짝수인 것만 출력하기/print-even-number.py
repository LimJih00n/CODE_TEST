N = int(input())
arr = list(map(int,input().split()))
arr = [i for i in arr if i%2==0]
print(*arr)