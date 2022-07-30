# 특정 문자열에서 "균형잡힌 괄호 문자열"의 인덱스를 반환하는 함수와
# 특정한 "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"인지 판단하는 함수 별도 구현
# 이후 재귀 함수에서 이 두함수를 불러오도록함

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0   # 왼쪽 괄호의 개수: "("
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# "올바른 괄호 문자열"인지 판단
def check_proper(p):
    count = 0   # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            # 쌍이 맞지 않는 경우 False(count가 0인 상태에서 ")"가 먼저 나오면 쌍이 안맞음)
            if count == 0: 
                return False
            count -= 1
    return True # 쌍이 맞는 경우 True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙혀 반환
    # "균형잡힌 괄호 문자열"이 "올바른 괄호 문자열"이라면
    if check_proper(u):
        answer = u + solution(v)
    # "올바른 괄호 문자열"이 아니라면 아래의 과정 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])   # 첫 번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer