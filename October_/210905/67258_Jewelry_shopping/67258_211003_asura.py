# 접근방법 : 해쉬 or two-point
# 문제에서 구역이 안나올 수 있다는 조건이 없기에, 무조건 나온다는 가정하에 풀이
# 현재 지정한 범위에 모든 보석이 들어오게 되면 범위를 줄일 수 있는지를 확인
# 그 후, 적절하게 left,right 범위 조정

def solution(gems):
    ans = []
    dic = {}

    set_gems = set(gems)
    left, right = 0, 0
    sect = int(1e9) # 이 부분떄문에 블로그 참조했음.

    while right < len(gems): # 끝 점이 범위 안에 있을 때 검사
        if gems[right] not in dic:
            dic[gems[right]] = 1
        else:
            dic[gems[right]] += 1

        right += 1 # 보석을 추가한 후 right 한칸 움직이기

        if len(dic) == len(set_gems): # set 크기와 dictionary 크기가 같다면
            while left < right:
                if dic[gems[left]] > 1:
                    dic[gems[left]] -= 1
                    left += 1
                elif sect > min(right - left, sect): # 더 큰 구간이 나올 수 있기 때문에 추가한 변수 sect
                    sect = right - left
                    ans = [left + 1, right]
                    break
                else:
                    break
    return ans