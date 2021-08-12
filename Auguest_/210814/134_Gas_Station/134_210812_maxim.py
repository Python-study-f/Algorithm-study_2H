from typing import List
import unittest


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = -1
        gas_size = len(gas)
        for i in range(gas_size):
            flag = True
            remain_gas = 0
            for j in range(i, i + gas_size):
                remain_gas += gas[j % gas_size] - cost[j % gas_size]
                if remain_gas < 0:
                    flag = False
                    break

            if flag:
                result = i
                break

        return result


# TestCase를 작성
# class MainTest(unittest.TestCase):
#     def test(self):
#         solution = Solution()
#         gas = [1, 2, 3, 4, 5]
#         cost = [3, 4, 5, 1, 2]
#         expected = solution.canCompleteCircuit(gas, cost)
#         result = 3
#
#         self.assertEqual(expected, result)
#
#
# # unittest를 실행
# if __name__ == '__main__':
#     unittest.main()
