# 1. 귀찮아서 일단 dfs로 완전탐색 돌려보니 5.02% 나옴;; 너무 느려서 다시 풀 예정
#  특이점 : ldfs 로 left 돌렸을때 남은 가스가 0이 되는 순간까지 카운트 해주지 않으면 틀림, rdfs로 오른쪽으로 돌릴 때는 0을 카운트 해주면 틀림
# 예시 테케 
# [5,1,2,3,4]
# [4,4,1,5,1]


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        def ldfs(idx, remain, cnt):
            print(idx, remain, cnt)
            if remain <= 0:
                return False
            if cnt > N:
                return True
            l = idx - 1
            if l < 0:
                l = N-1
            return ldfs(l, remain-cost[l]+gas[idx], cnt+1)
        
        def rdfs(idx, remain, cnt):
            if remain < 0:
                return False
            if cnt > N:
                return True
            r = idx + 1
            if r == N:
                r = 0
            return rdfs(r, remain-cost[idx]+gas[idx], cnt+1)

    
        for i in range(N):
            if ldfs(i, 0, 1):
                return i
            if rdfs(i, 0, 1):
                return i
        return -1
    
            
