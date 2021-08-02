def solution(s):
    dic={
        "zero" : 0 ,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    check = ""
    ans = []
    for i in range(len(s)):
        if s[i].isdigit():
            ans.append(s[i])
            continue

        check += s[i]

        if check in dic.keys():
            ans.append(str(dic.get(check)))
            check = ""

    return(int(''.join(ans)))