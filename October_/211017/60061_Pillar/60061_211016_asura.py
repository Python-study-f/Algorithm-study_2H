def check(result):
    for a in result:
        x, y, what = a

        if what == 0:  # 기둥일 경우
            if y == 0 or (x - 1, y, 1) in result or (x, y, 1) in result or (x, y - 1, 0) in result:
                continue
            else:
                return False
        else:  # 보일 경우
            if (x, y - 1, 0) in result or (x + 1, y - 1, 0) in result or (
                    (x - 1, y, 1) in result and (x + 1, y, 1) in result):
                continue
            else:
                return False

    return True


def solution(n, build_frame):
    result = set()

    for a in build_frame:
        x, y, what, how = a
        # print((x,y,what,how))
        if how == 1:
            result.add((x, y, what))
            is_boolean = check(result)

            if is_boolean:
                continue
            else:
                result.remove((x, y, what))
        else:
            result.remove((x, y, what))
            is_boolean = check(result)

            if is_boolean:
                continue
            else:
                result.add((x, y, what))

    return sorted(result, key=lambda x: (x[0], x[1], x[2]))