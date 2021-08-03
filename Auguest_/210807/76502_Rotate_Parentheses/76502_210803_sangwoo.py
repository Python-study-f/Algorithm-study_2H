def solution(s):
    count = 0
    a = list(s)
    b = []
    # 문자열의 길이만큼 왼쪽으로 회전
    for i in range(len(a)):
        # 먼저 카운트를 증가시킨다음 검사에서 틀린 경우가 나왔을때 다시 감소시킴
        count += 1
        for j in range(len(a)):
            # 괄호의 왼쪽이 나왔을때는 임시 리스트에 저장, 오른쪽이 나왔을때,
            # 해당 괄호의 왼쪽이 저장되어있을때는 그 괄호를 임시 리스트에서  제거 
            # 없을때는 카운트 감소, 임시리스트 초기화 후 break
            if a[j] in ['[', '{', '(']:
                b.append(a[j])
            else:
                if a[j] == '}' and '{' in b:
                    b.remove('{')
                elif a[j] == ']' and '[' in b:
                    b.remove('[')
                elif a[j] == ')' and '(' in b:
                    b.remove('(')
                else:
                    count -= 1
                    b = []
                    break
        temp = a.pop(0)
        a.append(temp)
    return count
