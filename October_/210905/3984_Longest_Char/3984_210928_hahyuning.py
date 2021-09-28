class Solution:
    def maxLength(self, arr):

        a = []
        for x in arr:
            if len(x) == len(set(x)):
                a.append(set(x))

        n = len(a)
        ans = 0

        def check(idx, s):
            nonlocal ans

            if idx == n:
                ans = max(ans, len(s))
                return

            t = a[idx]
            if not s.intersection(t):
                check(idx + 1, s.union(t))
            check(idx + 1, s)

        check(0, set())

        return ans

