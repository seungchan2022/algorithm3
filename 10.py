# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이
    m = len(a[0])   # 열 길이
    result = [[0] * n for _ in range(m)]    # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    # 자물쇠 늘린 길이의 최대 인덱스는
    # (원래 자물쇠 길이 * 3 - 1)이므로 2배 범위 까지만 돌아야함
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            # n: 원래 자물쇠 길이
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key)     # 열쇠 회전
        # 회전시킨 열쇠를 자물쇠의 중앙부분에 합치기
        for x in range(n + 2):
            for y in range(n + 2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 안맞으면 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x - i][y - j] -= key[i][j]
    return False
