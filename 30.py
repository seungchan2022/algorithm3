# 각각의 리스트를 길이에 따라 나누고 길이가 같은 리스트에서 이진 탐색 수행!

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 두개의 2차원 리스트 선언
array = [[] for _ in range(10001)]      # 모든 단어를 길이마다 나누어서 저장하기 위한 리스트('?'가 뒤에 오는 문자열 리스트)
reversed_array = [[] for _ in range(10001)]     # 모든 단어를 길이마다 나누어 뒤집어서 저장하기 위한 리스트('?'가 앞에 오는 문자열 리스트)

def solution(words, queries):
    answer = []
    for word in words:  # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word)   # 단어를 길이별로 삽입
        reversed_array[len(word)].append(word[::-1])    # 단어를 길이별로 뒤집어서 삽입

    for i in range(10001):  # 단어를 길이별로 리스트 정렬(이진탐색 수행하기 위해)
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:   # 쿼리를 하나씩 처리하며
        if q[0] != '?':     # 접미사(단어 뒤)에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:   # 접두사(단어 앞)에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer 
