import unittest


class Solution:
    def maxArea(self, height) -> int:
        memo = []
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                if height[i] > height[j]:
                    temp_height = height[j]
                else:
                    temp_height = height[i]

                memo.append(width * temp_height)

        return max(memo)


# TestCase를 작성
class MainTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        int_list = [1, 1]
        result = solution.maxArea(int_list)
        expected = 1

        self.assertEqual(result, expected)

    def test2(self):
        solution = Solution()
        int_list = [1, 2, 1]
        result = solution.maxArea(int_list)
        expected = 2
        self.assertEqual(result, expected)

    def test3(self):
        solution = Solution()
        int_list = [4, 3, 2, 1, 4]
        result = solution.maxArea(int_list)
        expected = 16
        self.assertEqual(result, expected)

    def test4(self):
        solution = Solution()
        int_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        result = solution.maxArea(int_list)
        expected = 49
        self.assertEqual(result, expected)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
