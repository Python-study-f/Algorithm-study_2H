# Gas Station 134 Leetcode


def canCompleteCircuit(gas, cost):
    ans = 0
    totsum = 0
    ixsum = 0
    for i in range(len(gas)):
        ixsum += gas[i] - cost[i]
        totsum += gas[i] - cost[i]
        if ixsum < 0:
            ans = i + 1
            ixsum = 0
    if totsum < 0:
        ans = -1
    return ans


# gas = [2, 3, 4]
# cost = [3, 4, 3]

# print(canCompleteCircuit(gas, cost))
