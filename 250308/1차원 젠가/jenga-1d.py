n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.
'''
what? 두번의 구간을 없앴을때 남은 block 구하기
how?: s1번째이므로 1~N인것을 주의한다.
그냥 그 부분제외하고 배열 다시 만들고 또 한번더 반복
0~s1
e1~len(blocks)
2번째~3번째까지 빼기 => idx: 1 ~ 2
따라서 합칠때는 [0:s1-1], [e1,n]
idx  0 1 2 3 4
번째 1 2 3 4 5
2~3
0 : 1 3~4
'''

blocks = blocks[0:s1-1] + blocks[e1:n]
blocks = blocks[0:s2-1] + blocks[e2:len(blocks)]

print(len(blocks))
for n in blocks:
    print(n)

