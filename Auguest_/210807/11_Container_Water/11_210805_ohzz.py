# Container_Water 11 릿코드


def maxArea(height):
    lt, rt = 0, len(height) - 1
    res = 0

    while lt < rt:
        cur_value = min(height[lt], height[rt])
        cur_area = (rt - lt) * cur_value
        res = max(res, cur_area)

        if height[lt] > height[rt]:
            rt -= 1
        else:
            lt += 1
    return res


print(maxArea([1, 2, 1]))
