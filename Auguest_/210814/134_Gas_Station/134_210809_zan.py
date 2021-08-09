# n개의 주유소가 순환 루트로 있고, i번째 주유소의 주유량은 gas[i].
# 당신은 무제한의 주유통을 가지고 있다. i 번 째에서 i+1 번 째 주유소까지 가는데는 cost[i] 만큼의 기름이 사용된다.
# 당신은 비어있는 주유통을 가지고 한 주유소에서 여정을 시작한다.
# gas array, cost array가 주어질 때, 시계 방향으로 모든 루트를 돌 수 있는 시작 점을 반환하라. 없을 경우, -1을 반환한다.

# 1 <= n <= 10000
# len(gas)==n, len(cost)==n
# 0 <= gas[i], cost[i] <= 10000

# REF https://m.blog.naver.com/jjys9047/222102423412
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1

        cs, start = 0, 0
        for i in range(n):
            cs += gas[i] - cost[i]
            if cs < 0:
                cs = 0
                start = i + 1
        return start
