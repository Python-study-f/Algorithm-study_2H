# 주어진 문자열을 리스트에 문자 하나씩 저장한 뒤 차례대로 꺼내어 비교해가면서 순자를 완성
def solution(s):
    tempAnswer = []
    temp = []
    a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # 비교할 리스트
    b = list(s)
    for i in range(len(b)):
        # 해당 값이 숫자일때 정답 리스트에 그대로 저장
        if b[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            tempAnswer.append(b[i])
        # 문자열일 경우 임시 리스트에 저장한뒤, 만약 리스트의 문자들을 모아봐서
        # 비교할 리스트에 있는 문자로 완성될 경우 숫자로 치환한 뒤 저장
        else:
            temp.append(b[i])
            if "".join(temp) in a:
                strTemp = "".join(temp)
                tempAnswer.append(str(a.index(strTemp)))
                temp = []
    answer = int("".join(tempAnswer))
    return answer
