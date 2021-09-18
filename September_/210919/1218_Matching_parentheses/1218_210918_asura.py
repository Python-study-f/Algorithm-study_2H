T = 10

dic = { "{" : "}" , "<":">", "[":"]","(":")"} # key - value로 값 체크 dictionary 생성

for tc in range(1,T+1):
    st = [] # Stack으로 체크할 것임
    not_necessary = int(input())
    ans = 0
    data = list(map(str,input()))

    for c in data:
        if c in dic:
            st.append(c)

        else:
            if st:
                check = st[-1]

                if dic[check] != c:
                    break
                else:
                    st.pop()
    else:
        ans = 1

    print("#{} {}".format(tc,ans))