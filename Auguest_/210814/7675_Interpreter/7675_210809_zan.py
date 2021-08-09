# 외국 대사는 총 N개의 문장을 말했다.
# 각 문장의 마지막 단어는 ./?/! 중 하나를 포함한다.
# 문장은 대소문자 알파벳, 숫자로 이루어진 단어들이 공백을 사이에 두고 구성되어 있다.
# 이름은 대문자로 시작하여 나머지는 소문자이다.
# 이름이 몇 번 나오는지를 알려줘야 한다.
# 문장 별로 이름의 개수를 구하라.

import re

T = int(input())

for tc in range(T):
    n = int(input().strip())
    sens = re.split(r" ?[.?!]+", input())[:-1]
    names = []
    for s in sens:
        words = list(map(lambda w: re.fullmatch(r"[A-Z]{1}[a-z0-9]*", w), s.split()))
        names.append(sum(x is not None for x in words))

    print(f"{tc+1}", end=" ")
    print(*names)
