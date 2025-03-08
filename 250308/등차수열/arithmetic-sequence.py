'''
what? K를 정해서
ai,K,aj => 3개 등차수ㅕㄹ 이루도록 하는
K 정하기. 저 3개 튜플 조합의 개수 구하기. 

how?
1) 입력 받은 거 정렬
2) min수~max수 넣고 정렬
3) 등차 수열 개수 구하기 => 
ex: 3 4 5 6 7 에서 등차 수열의 개수를 어떻게 구할 수 있나??
idx로 넣어야한다. 
! 넣은 수가 가운데여야함
let 넣은 수가 n일때
넣은 수가 가운데 이고 양옆의 수는 모두 넣어서 
아니면 그냥 가운데는 고정하고. 양옆은 있는 수 모두 넣어서 확인하기
적은 거 큰거로 나뉘어서. small,big 으로 반복문 진행
등차 수열인지 확인 => (a + c) / 2 = b
'''
N = int(input())
arr = list(map(int,input().split()))
min_a = min(arr)
max_a = max(arr)
arr.sort()
ans = 0
max_count = 0
for n in range(min_a,max_a):

    count = 0
    small_a = [a for a in arr if a<n]
    big_a =  [a for a in arr if a>n]
    if len(small_a) == 0 or len(big_a) == 0:
        continue
    for a in small_a:
        for c in big_a:
            if (a+c)/2 == n:
                count +=1
    ans = max(ans,count)
print(ans)
