class Solution:
    def maxLength(self, arr: List[str]) -> int:
        words = []
        for a in arr:
            if len(set(list(a))) == len(a):
                words.append(a)
        
        def dfs(idx, s):
            if idx == len(words):
                return len(s)           
            for w in words[idx]:
                if w in s:
                    return dfs(idx+1, s)
            else:
                return max(dfs(idx+1, s), dfs(idx+1, s+words[idx]))
        return dfs(0, "")
