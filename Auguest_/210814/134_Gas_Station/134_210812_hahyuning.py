class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        now = 0
        for i in range(len(gas)):
            if now + gas[i] < cost[i]:
                start = i + 1
                now = 0
            else:
                now += (gas[i] - cost[i])
        return start