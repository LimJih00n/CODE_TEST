A = input()

# Please write your code here.
'''
what: 
쌍의 개수를 세는데 가능한 가짓수를 모두 세야한다. 열렸는지 닫혔는지 보는게 아님.
2개의 쌍 => 2개 열려 있는 거 찾기 -> 연속해야함
how: 완전 탐색 -> 만약  ( 를 찾으면, (( 를 찾으면 다음거 찾기
'''
count = 0
ans = 0

for i in range(1,len(A)):
    if A[i-1] =="(" and A[i] =="(":
        for j in range(i+1,len(A)):
            if A[j-1] ==")" and A[j] ==")":
                ans+=1
print(ans)