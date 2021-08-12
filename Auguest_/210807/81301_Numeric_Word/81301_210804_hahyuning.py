def solution(s):
    ans = ""
    prev = ""
    num = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for x in s:
        if prev in num:
            ans += num[prev]
            prev = ""

        if x.isdigit():
            if prev != "":
                ans += num[prev]
                prev = ""
            ans += x
        else:
            prev += x

    if prev != "":
        ans += num[prev]

    return int(ans)
