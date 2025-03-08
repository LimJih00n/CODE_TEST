n, m, t = map(int, input().split())

# Create n x n grid
arr = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]
marbles = [(r1, c1) for r1, c1 in zip(r, c)]

# 이동 방향 (상, 하, 좌, 우 순서)
move_dir = [
    (-1, 0),  # 상
    (1, 0),   # 하
    (0, -1),  # 좌
    (0, 1)    # 우
]

# 경계 체크 함수
def check_b(r, c):
    return 0 <= r < n and 0 <= c < n

# t초 동안 이동 실행
for _ in range(t):
    new_positions = {}  # 이동 후 위치 저장
    move_count = {}  # 위치별 구슬 개수 체크

    for mr, mc in marbles:
        max_val = arr[mr][mc]
        move_p = (mr, mc)

        for dr, dc in move_dir:
            nr, nc = mr + dr, mc + dc
            if check_b(nr, nc) and arr[nr][nc] > max_val:
                max_val = arr[nr][nc]
                move_p = (nr, nc)

        # 이동 위치 저장 (딕셔너리 사용)
        if move_p not in new_positions:
            new_positions[move_p] = (mr, mc)
            move_count[move_p] = 1
        else:
            move_count[move_p] += 1  # 충돌 발생

    # 충돌하지 않은 구슬만 남기기
    marbles = [new_positions[pos] for pos in new_positions if move_count[pos] == 1]

# 남아있는 구슬 개수 출력
print(len(marbles))
