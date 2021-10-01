class Solution:
    def maxLength(self, arr):

        arr = [i for i in arr if len(i) == len(set(i))]

        def dfs(idx, data):
            if idx == len(arr):
                return len(data)

            if not (set(data) & set(arr[idx])):
                return max(dfs(idx + 1, data + arr[idx]), dfs(idx + 1, data))
            else:
                return dfs(idx + 1, data)

        return dfs(0, "")
