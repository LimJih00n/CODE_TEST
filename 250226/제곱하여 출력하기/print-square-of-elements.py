N = int(input())
arr = map(int,input().split())
arr = [n**2 for n in arr]
print(*arr)