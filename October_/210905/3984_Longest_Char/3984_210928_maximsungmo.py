class Solution(object):
    def isIndependentChar(self, word):
        charset = set()
        for char in word:
            charset.add(char)
        if len(charset) == len(word):
            return True
        return False

    def maxLength(self, arr):
        result = 0
        word_dp = []
        # 주어진 배열에서 사용 가능한 값 추림
        for word in arr:
            if self.isIndependentChar(word):
                word_dp.append(word)
                result = max(result, len(word))

        if len(word_dp) == 0:
            return 0

        index = 0
        copy_word_dp = word_dp.copy()
        for primary in copy_word_dp:
            index = index + 1

            for iter in word_dp[index:]:
                temp_word = primary + iter
                if self.isIndependentChar(temp_word):
                    word_dp.append(temp_word)
                    result = max(result, len(temp_word))

        return result

# sol = Solution()
# arr = ["cha", "r", "act", "ers"]
# result = 6
# print(result == sol.maxLength(arr))
#
# arr = ["abcdefghijklmnopqrstuvwxyz"]
# result = 26
# print(result == sol.maxLength(arr))
#
# arr = ["a", "abc", "d", "de", "def"]
# result = 6
# print(result == sol.maxLength(arr))
#
# arr = ["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]
# result = 16
# print(result == sol.maxLength(arr))
