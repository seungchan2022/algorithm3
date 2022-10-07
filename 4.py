n = int(input())

array = list(map(int, input().split()))
array.sort()

target = 1
for i in array:
    if target < i:
        break
    target += i

print(target)


"""
주어진 화폐 단위를 하나씩 loop를 도는데,
이때 동시에 만들수 없는 금액을 1원부터 시작해서 특정 조건에 부합하면 바로 break
특정 조건: 만들기 가능 여부 확인 금액(target) < 확인 하려는 화폐 단위

ex) N = 4  array = [1, 2, 3, 8]

    1 ~ target - 1까지 모든 금액을 만들 수 있다고 가정!!

    1) 처음에 금액 1을 만들 수 있는 지 확인 하기 위해, target = 1로 설정

    2) target = 1을 만족하는지 확인. 화폐 단위가 1인 동전이 있으므로 1을 만들 수 있음(target >= 확인 하려는 단위를 만족 하므로).
        target = 1 + 1 = 2로 갱신 -> 1(target - 1)까지의 모든 금액을 만들 수 있음
            (만들기 가능 여부 확인 금액(target) + 사용한 화폐 단위)
    
    3) target = 2를 만족하는지 확인. 화폐 단위가 2인 동전이 있으므로 2를 만들 수 있음.
        target = 2 + 2 = 4로 갱신 -> 3까지 모든 금액을 만들 수 있음
    
    4) target = 4를 만족하는지 확인. 화폐 단위가 3인 동전이 있음
        target = 4 + 3 = 7로 갱신 -> 6까지 모든 금액을 만들 수 있음
    
    5) target = 7을 만족하는지 확인. 화폐 단위 7보다 큰 8이 있음.
        target < 확인 하려는 화폐 단위 이므로 brak
        이때, target 값이 정답
"""