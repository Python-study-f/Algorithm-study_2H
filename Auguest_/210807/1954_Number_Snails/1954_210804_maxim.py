from typing import List
import unittest


class Solution:
    def number_snail(self, N) -> List[int]:
        # init value
        x = -1
        y = 0
        result = [[0 for col in range(N)] for row in range(N)]
        # R, D, L, U
        direction = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        count = 0

        while count < (N ** 2):
            will_move_x = x + dx[direction % 4]
            will_move_y = y + dy[direction % 4]
            if (-1 < will_move_x < N) and (-1 < will_move_y < N) and result[will_move_y][will_move_x] == 0:
                count += 1
                x = will_move_x
                y = will_move_y
                result[y][x] = count
            else:
                direction += 1

        for i in range(len(result)):
            result_row = ','.join(str(_) for _ in result[i])
            print(result_row)

        return result


T = 3
solution = Solution()
for test_case in range(1, T + 1):
    print(f"#{test_case}")
    solution.number_snail(test_case)


# TestCase를 작성
class MainTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        N = 2
        snail = [
            [1, 2],
            [4, 3],
        ]
        result = solution.number_snail(N)

        self.assertEqual(snail, result)

    def test2(self):
        solution = Solution()
        N = 3
        snail = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        result = solution.number_snail(N)

        self.assertEqual(snail, result)

    def test3(self):
        solution = Solution()
        N = 4
        snail = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        result = solution.number_snail(N)

        self.assertEqual(snail, result)

    def test4(self):
        solution = Solution()
        N = 5
        snail = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        result = solution.number_snail(N)

        self.assertEqual(snail, result)

    def test5(self):
        solution = Solution()
        N = 6
        snail = [
            [1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11]
        ]
        result = solution.number_snail(N)

        self.assertEqual(snail, result)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
