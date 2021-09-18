for T in range(10):
    answer = 1
    p = {"[": "]", "{": "}", "(": ")", "<": ">"}
    stack = []

    N = int(input())
    string = input().strip()
    for char in string[::-1]:
        if char in p.values():
            stack.append(char)
            continue
        if not stack or stack[-1] != p[char]:
            answer = 0
            break
        stack.pop()

    print(f"#{T+1} {answer}")
