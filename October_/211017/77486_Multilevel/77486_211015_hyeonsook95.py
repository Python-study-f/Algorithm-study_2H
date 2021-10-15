def solution(enroll, referral, seller, amount):
    answer = {s: 0 for s in enroll}
    referral = {s: r for s, r in zip(enroll, referral)}

    def btrack(amt, slr):
        while slr != "-" and amt > 0:
            commission = amt // 10
            answer[slr] += amt - commission

            amt = commission
            slr = referral[slr]
        return

    for slr, amt in zip(seller, amount):
        answer[slr] += amt * 90
        if referral[slr] != "-" and amt * 10 > 0:
            btrack(amt * 10, referral[slr])

    return list(answer.values())
