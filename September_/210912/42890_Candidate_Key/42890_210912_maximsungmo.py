from itertools import combinations


def is_include(list1, list2):
    results = []
    for s1 in list1:
        if s1 in list2:
            results.append(s1)

    return results == list1


def solution(relation):
    answer = 0
    column_no_list = [i for i in range(len(relation[0]))]
    comb_column_no_list = []

    if len(relation) > 0:
        row_length = len(relation)
        column_length = len(relation[0])

        # 전체 조합 찾기
        for i in range(1, column_length + 1):
            comb_column_no_list.extend(list(combinations(column_no_list, i)))

        # 1. 유일성 체크
        check_columns = []
        for column_tuple in comb_column_no_list:
            distinct_row_count = set()

            # 2. 최소성 체크, 최소성에 어긋나면 굳이 계산할 필요없이 건너뜀
            flag = False
            for check in check_columns:
                if is_include(check, list(column_tuple)):
                    flag = True
                    break
            if flag:
                continue

            for i in range(row_length):
                col_as_str = ''
                for j in column_tuple:
                    col_as_str += relation[i][j]
                distinct_row_count.add(col_as_str)

            if len(distinct_row_count) == row_length:
                check_columns.append(list(column_tuple))

        return len(check_columns)
