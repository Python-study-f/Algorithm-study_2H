def inbox(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    else:
        return False

def solution(places):
    answer = []
    for place in places:
        state = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if inbox(i + 1, j) and place[i + 1][j] == "P":
                        state += 1
                    if inbox(i + 2, j) and place[i + 2][j] == "P" and place[i + 1][j] != "X":
                        state += 1
                    if inbox(i, j + 1) and place[i][j + 1] == "P":
                        state += 1
                    if inbox(i, j + 2) and place[i][j + 2] == "P" and place[i][j + 1] != "X":
                        state += 1
                    if inbox(i + 1, j + 1) and place[i + 1][j + 1] == "P" and (place[i + 1][j] != "X" or place[i][j + 1] != "X"):
                        state += 1
                    if inbox(i + 1, j - 1) and place[i + 1][j - 1] == "P" and (place[i][j - 1] != "X" or place[i + 1][j] != "X"):
                        state += 1
        if state == 0:
            answer.append(1)
        else:
            answer.append(0)
    return answer
