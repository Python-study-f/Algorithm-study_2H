from collections import deque


def solution(s):
    ans = []

    for s_ in s:
        st = []
        cnt = 0

        for c in s_:  # 110을 빼는데, 뺴고나서도 110이 생기면 그걸 cnt에 넣는다.
            if c == '0':
                if st[-2:] == ['1', '1']:
                    cnt += 1
                    st.pop()
                    st.pop()
                else:  # 0이지만, 앞에 2개가 11이 아닐 경우
                    st.append(c)
            else:  # 문자가 0이 아니라면
                st.append(c)

        if cnt == 0:  # 애초부터 110이 아예 없었다면 ans에 그냥 s 값 그대로 넣기
            ans.append(s_)

        else:  # 110 있다면
            dq = deque()

            while st:  # append로 넣은 st에 0이 나올때까지
                if st[-1] == "1":
                    dq.append(st.pop())
                else:  # 0이였을 때
                    break

            while cnt > 0:  # 반복횟수만큼
                dq.appendleft('0')
                dq.appendleft('1')
                dq.appendleft('1')
                cnt -= 1

            while st:
                dq.appendleft(st.pop())
            ans.append(''.join(dq))

    return ans