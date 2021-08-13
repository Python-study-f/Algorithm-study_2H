import unittest

table = []


def solution(info, query):
    answer = []
    for i in info:
        table.append(i.split())
    table.sort(key=lambda row: int(row[4]), reverse=True)
    for q in query:
        answer.append(get_count_by_filter_using_query(q))
    return answer


def get_count_by_filter_using_query(query):
    query = query.replace(" and ", " ").split(" ")
    count = 0
    for t in table:
        if int(t[4]) < int(query[4]):
            break
        if (query[0] == "-" or t[0] == query[0]) and \
                (query[1] == "-" or t[1] == query[1]) and \
                (query[2] == "-" or t[2] == query[2]) and \
                (query[3] == "-" or t[3] == query[3]):
            count += 1

    return count


# TestCase를 작성
class MainTest(unittest.TestCase):
    def test(self):
        info = ["java backend junior pizza 150", "python frontend senior chicken 210",
                "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80",
                "python backend senior chicken 50"]
        query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                 "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                 "- and - and - and chicken 100", "- and - and - and - 150"]
        expected = solution(info, query)
        result = [1, 1, 1, 1, 2, 4]
        self.assertEqual(expected, result)


# unittest를 실행
if __name__ == '__main__':
    unittest.main()
