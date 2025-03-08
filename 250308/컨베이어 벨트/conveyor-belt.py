n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
'''
what? T초후의 컨베이어 벨트 상태구하기 
컨베이어 벨트? u ,d 로 구성
1초마다 u -> , d <- ,u[-1] ->d[-1], d[0] -> u[0]
how?
컨베이어 벨트 구현하기
temp1 = u[-1]
temp2 = d[0]
move: u[0:n] => u[1:n]
mve : d[1:n] => d[0:n-1]
돌리는 거 주의해야함
'''
d = d[::-1]
while True:
    temp1 = u[-1]
    temp2 = d[0]
    u = [temp2]+u[0:n-1]
    d = d[1:n]+[temp1]
    t -= 1
    if t==0:
        break
print(*u)
print(*d[::-1])