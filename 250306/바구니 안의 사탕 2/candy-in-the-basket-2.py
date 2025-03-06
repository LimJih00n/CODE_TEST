N, k = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
'''
what? 특정 범위 이내의 사탕 개수를 합의 최대를 구하는 것. 
how? 1. 사탕 배열 만들기 => 0은 없음 n은 있음 idx가 좌표
     2. 처음 부터 끝까지 돌면서 +- k 의 case를 합하기
     3. max 찾기
    cf: 같은 위치에 여러개가 놓여있을 수도 있음

'''
candys = [0]*101
for c,p in zip(candy,pos):
    candys[p] += c
ans = 0
for i in range(101):
    k_ = k if i- k >=0 else i 
    k__ = k if i+k <101 else 100
    ans = max(ans,sum(candys[i-k_:i+k__+1]))
print(ans)