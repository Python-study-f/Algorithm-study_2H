def check(ans):
    for x, y, stuff in ans:
        # 기둥: 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 다른 기둥 위
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in ans or [x, y, 1] in ans or [x, y - 1, 0] in ans:
                pass
            else:
                return False
        # 보: 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결
        else:
            if [x, y - 1, 0] in ans or [x + 1, y - 1, 0] in ans or ([x - 1, y, 1] in ans and [x + 1, y, 1] in ans):
                pass
            else:
                return False
    return True


def solution(n, build_frame):
    ans = []

    for x, y, stuff, op in build_frame:
        # 0 삭제, 1 설치
        if op == 0:
            ans.remove([x, y, stuff])

            if not check(ans):
                ans.append([x, y, stuff])
        else:
            ans.append([x, y, stuff])

            if not check(ans):
                ans.pop()

    return sorted(ans)