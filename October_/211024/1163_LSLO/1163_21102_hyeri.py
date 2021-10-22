
class Solution(object):
    def lastSubstring(self, s):
        left, right, i = 0, 1, 0
        while right+i < len(s):
            if s[left+i] == s[right+i]:
                i += 1
                continue
            if s[left+i] > s[right+i]:
                right += i+1
            else:
                left = max(right, left+i+1)
                right = left+1
            i = 0
        return s[left:]
