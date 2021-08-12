# 숫자 문자열과 영단어 81301 프로그래머스


def solution(s):
    dict_num = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for k, v in dict_num.items():
        s = s.replace(k, v)

    return s


print(solution("one4seveneight"))
