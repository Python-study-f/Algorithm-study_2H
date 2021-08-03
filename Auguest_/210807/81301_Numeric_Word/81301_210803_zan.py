# 81301 숫자 문자열과 영단어

# 네오가 프로도에게 숫자를 건넬 때, 일부 자릿수의 숫자를 영단어로 바꾼 카드를 주면 프로도가 원래 숫자를 찾는 게임이다.
# 숫자 일부 자릿수가 영단어로 바뀌었거나, 바뀌지 않고 그대로인 문자열 s가 주어진다.
# s를 원래 숫자로 return 하는 solution 함수를 완성하라.

# 입력
# s, 문자열, 1 <= len(s) <= 50
# s는 0 or zero로 시작하지 않는다.
# answer, 1 <= answer <= 2,000,000,000


def solution(s):
    num_dict = {
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
    for ch, num in num_dict.items():
        s = s.replace(ch, num)
    return int(s)
