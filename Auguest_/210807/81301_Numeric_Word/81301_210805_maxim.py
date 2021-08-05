import unittest

word_dictionary = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solution(s):
    for word, number in word_dictionary.items():
        s = s.replace(word, str(number))
    return int(s)


# TestCase를 작성
class MainTest(unittest.TestCase):
    def test(self):
        s = "one4seveneight"
        expected = 1478
        result = solution(s)
        self.assertEqual(expected, result)

    def test2(self):
        s = "23four5six7"
        expected = 234567
        result = solution(s)
        self.assertEqual(expected, result)

    def test3(self):
        s = "2three45sixseven"
        expected = 234567
        result = solution(s)
        self.assertEqual(expected, result)

    def test4(self):
        s = "123"
        expected = 123
        result = solution(s)
        self.assertEqual(expected, result)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
