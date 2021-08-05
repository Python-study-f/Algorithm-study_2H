import unittest

open_case = ["{", "[", "("]
close_case = ["}", "]", ")"]
match_case = {
    "{": "}",
    "(": ")",
    "[": "]"
}


def solution(s):
    count = 0
    for i in range(len(s)):
        temp = s[i:] + s[0:i]
        if is_right(temp):
            count += 1
    return count


def is_right(s):
    stack = []
    for char in s:
        if char in open_case:
            stack.append(char)
        if char in close_case:
            if len(stack) == 0: return False
            peek = stack.pop()
            if char != match_case[peek]:
                return False
    if len(stack) != 0: return False
    return True


# TestCase를 작성
class MainTest(unittest.TestCase):
    def test(self):
        s = "[](){}"
        expected = 3
        result = solution(s)
        self.assertEqual(expected, result)

    def test2(self):
        s = "}]()[{"
        expected = 2
        result = solution(s)
        self.assertEqual(expected, result)

    def test3(self):
        s = "[)(]"
        expected = 0
        result = solution(s)
        self.assertEqual(expected, result)

    def test4(self):
        s = "}}}"
        expected = 0
        result = solution(s)
        self.assertEqual(expected, result)

    def test5(self):
        s = "{{{"
        expected = 0
        result = solution(s)
        self.assertEqual(expected, result)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
