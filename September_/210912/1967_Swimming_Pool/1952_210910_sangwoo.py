a = int(input())
for k in range(a):
    ticket = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    price = [0 for _ in range(13)]
    for i in range(12):
        if i == 0:
            price[i] = min(ticket[0] * plan[i], ticket[1])
        elif i == 2:
            price[i] = min(ticket[0] * plan[i], ticket[1]) + price[i-1]
            price[i] = min(price[i], ticket[2] + price[i-2])
        elif i > 2:
            price[i] = min(ticket[0] * plan[i], ticket[1]) + price[i-1]
            price[i] = min(price[i], ticket[2] + price[i-3])
        else:
            price[i] = min(ticket[0] * plan[i], ticket[1]) + price[i-1]
    answer = min(price[11], ticket[3])
    print('#{} {}'.format(k + 1, answer))
