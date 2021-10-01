from itertools import combinations

class Solution(object):
    def maxLength(self, arr):   
        answer = 0
        for n in range(len(arr)):
            for words in combinations(arr, n + 1):
                word = ''.join(words)
                if len(word) == len(set(word)):
                    answer = max(answer, len(word))
                
        return answer
