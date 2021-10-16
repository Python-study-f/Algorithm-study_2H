import math

def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    tree = {}
    for i in range(len(enroll)):
        tree[enroll[i]] = (referral[i], i)
    for i in range(len(seller)):
        price = 100 * amount[i]
        referralperson, pos = tree[seller[i]]
        benefit = math.floor(price / 10)
        answer[pos] += price - benefit
        while benefit != 0 or tree[seller[i]] != "-":
            price = benefit
            referralperson, pos = tree[referralperson]
            benefit = math.floor(price / 10)
            answer[pos] += price - benefit
    return answer
