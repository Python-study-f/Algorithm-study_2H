import re


def count_name(input_data, ans=[]):
    end_signal = [".", "!", "?"]
    regex = re.compile("[A-Z]+[a-z]*[.?!]?")
    word_list = input_data.split(" ")
    count = 0
    for word in word_list:
        if regex.fullmatch(word):
            count += 1
        for signal in end_signal:
            if word.endswith(signal):
                ans.append(str(count))
                # 값 초기화
                count = 0
                break


T = int(input())
for test_case in range(1, T + 1):
    word_count = int(input())
    input_data = input()
    answer = []
    count_name(input_data, answer)
    print("#{}".format(test_case), end=" ")
    print(*answer)
