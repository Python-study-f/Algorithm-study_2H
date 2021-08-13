T = int(input())

for tc in range(T):
    sentence_cnt = int(input())

    sentence = input()
    idx, ans = 0, []

    for i in range(len(sentence)):
        if sentence[i] in ('!','?','.'):
            cnt = 0
            for word in sentence[idx:i].split():
                if (len(word) == 1 and word[0].isupper()) or (word.isalpha() and word[0].isupper() and word[1:].islower()):
                    cnt += 1
            idx = i + 2 # 공백까지 처리
            ans.append(cnt)

    print(f'#{tc + 1}', *ans)
