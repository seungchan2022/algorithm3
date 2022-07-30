def solution(s):
    answer = len(s)
    # 1개 단위부터 압축단위(step)를 len(s)//2 까지 늘려가며 확인(그이상은 압축 할수 X)
    for step in range(1, len(s) // 2 + 1):
        result = " "
        prev = s[0:step] # 앞에서 부터 step 만큼 문자열 추출
        count = 1   # 압축 횟수
        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for i in range(step, len(s), step):
            # 이전 상태와 동일 하다면 count 증가
            if prev == s[i:i + step]:
                count += 1
            else:
                result += str(count) + prev if count >= 2 else prev     # count = 1이면 생략
                prev = s[i:i + step]     # 초기화
                count = 1
        # 남아 있는 문자열 처리
        result += str(count) + prev if count >= 2 else prev     
        # 만들어 지는 압축 문자열이 가장 짧은것
        answer = min(answer, len(result))
    return answer
