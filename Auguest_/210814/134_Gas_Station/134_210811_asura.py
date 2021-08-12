## 문제 해설 블로그 : https://ihp001.tistory.com/124 코드 참조 X ##
##                  문제 선정 누가한거야 ^-^;;;                 ##

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        tank, index = 0, -1
        if sum(cost) > sum(gas):
            print(-1)

        for i in range(len(gas)):
            if tank + gas[i] >= cost[i]:
                if tank == 0:
                    index = i
                tank += gas[i] - cost[i]
            else:
                tank, index = 0 , -1
        return index

"""
TC중에 
[1,2,3,4,5]
[3,4,5,1,2]
가 해당 케이스 해결방법을 gas 합 < 연료 사용량 이면  -1 반환
"""