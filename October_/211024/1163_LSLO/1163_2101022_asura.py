
# 문제 오류가 있는 것 같습니다,,, 제대로 선별할게요 ㅠㅠ
# 킹받네,,
# https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/361121/Python-O(n)-with-explanation
class Solution:
    def lastSubstring(self, s: str) -> str:
        count = collections.defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        largeC = max(count.keys())
        starts = {}
        for pos in count[largeC]:
            starts[pos] = pos + 1
        # Initialize all candidates and their pointers

        while len(starts) > 1:
            # Eliminate till we have only one
            toDel = set()
            nextC = collections.defaultdict(list)
            for start, end in starts.items():
                if end == len(s):
                    # Remove if reaching the end
                    toDel.add(start)
                    continue

                nextC[s[end]].append(start)
                # Filter by current letter

                if end in starts:
                    toDel.add(end)
                # "Swallow" the latter candidate

            nextStarts = {}
            largeC = max(nextC.keys())
            for start in nextC[largeC]:
                if start not in toDel:
                    nextStarts[start] = starts[start] + 1
                # Select what we keep for the next step
            starts = nextStarts.copy()
        for start, end in starts.items():
            return s[start:]
# TLE
# def getMax(string):
#     alpha = string[0]
#     index_lst = [0]
#
#     for i in range(1, len(string)):
#         if string[i] == alpha:
#             index_lst.append(i)
#
#         elif string[i] > alpha:
#             index_lst = [i]
#             alpha = string[i]
#     return index_lst, alpha
#     # cur은 가장 랭크가 높은 알파벳, ret는 해당 index 저장
#
#
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#         if len(set([z for z in s])) == 1:
#             return s
#
#         idx, alp = getMax(s)
#         cur = idx
#
#         if len(idx) == 1:
#             return s[idx[0]:]
#
#         while True:
#             cur = [a + 1 for a in cur if a + 1 < len(s)]
#             if not cur:
#                 break
#
#             _max = max([s[i] for i in cur])
#             alp += _max
#             cur = [i for i in cur if s[i] == _max]
#         return alp

# 7376ms / 18MB
# len(s) == 1 없으면 시간초과.
# class Solution:
#     def lastSubstring(self, s: str) -> str:
#
#         tmp = s
#         if len(s) == 1:
#             return s
#
#         for i in range(1, len(s)):
#             if s[i:] > tmp:
#                 tmp = s[i:]
#         return tmp