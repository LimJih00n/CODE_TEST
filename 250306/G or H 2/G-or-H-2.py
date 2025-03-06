n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
'''
what? G,H,0로 이루어진 배열의 연속 부분 집합에서 G,H 개수가 같거나 한쪽으로만 이루어진
배열의 길이 구하기. 하나만 있는 경우는 0

how: 
n이 100단위라 ff도 가능하다. 
1. 구간 정하기 pos중 제일 작은 값과 제일 큰 값 사이의 경우 
   2개의 수 뽑기(조합으로) => 이중 반복문
2. 2개 구간으로 이루어진 배열 만들고 조건 확인
    1. 개수 같은지
    2. 한쪽인지
3. 조건 맞족시 크기 비교
'''
def check_condtion(a):
    if "G" in a and "H" in a and a.count("G")==a.count("H"):
        return True
    if "G" in a and "H" not in a:
        return True
    if "H" in a and "G" not in a:
        return True
    return False
        

arr = [0]*101
min_x,max_x = min(pos),max(pos)

for pos,alpha in zip(pos,alpha):
    arr[pos] =alpha
ans = 0
for i in range(min_x,max_x+1):
    if arr[i] ==0:
        continue
    for j in range(i,max_x+1):
        if arr[j] ==0:
            continue
        check_arr = arr[i:j+1]
        
        if check_condtion(check_arr):
            ans = max(ans,j-i)
print(ans)

