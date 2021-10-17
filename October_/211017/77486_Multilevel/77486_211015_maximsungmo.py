def solution(enroll, referral, seller, amount):
    answer = []
    index = 0
    profit_dict = init_result(enroll)
    pc_dict = get_parent_child_dict(enroll, referral)
    for sell in seller:
        target = sell
        temp_profit = amount[index] * 100
        flag = True

        while flag and temp_profit > 0:
            profit_dict[target] += temp_profit
            child = target
            target = pc_dict[target]
            if target == '-':
                flag = False
            commission = temp_profit // 10
            profit_dict[child] -= commission
            temp_profit = commission

        index = index + 1
    return list(profit_dict.values())


def init_result(enroll):
    profit = dict()
    for _ in enroll:
        profit[_] = 0
    return profit


def get_parent_child_dict(enroll, referral):
    pc_dict = dict()
    index = 0
    for child in enroll:
        pc_dict[child] = referral[index]
        index = index + 1
    return pc_dict


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
result = [360, 958, 108, 0, 450, 18, 180, 1080]

assert result == solution(enroll, referral, seller, amount)
