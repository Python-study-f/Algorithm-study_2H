# 개똥벌레 3090 백준

# 첫 번째 풀이, 누적합
# pypy3 통과
# python3 시간초과...
n, h = map(int, input().split())

stone_top_map = [0] * (h + 1)
stone_bottom_map = [0] * (h + 1)
result = [0] * (h + 1)

for i in range(1, n + 1):
    k = int(input())
    if i % 2 == 0:
        stone_top_map[h - k + 1] += 1
    else:
        stone_bottom_map[k] += 1

for i in range(2, h + 1, +1):
    stone_top_map[i] += stone_top_map[i - 1]
for i in range(h - 1, 0, -1):
    stone_bottom_map[i] += stone_bottom_map[i + 1]

for i in range(1, h + 1):
    result[i] = stone_top_map[i] + stone_bottom_map[i]

result = result[1:]
min_num = min(result)
min_num_count = result.count(min_num)
print(result)
print(min_num, min_num_count)
