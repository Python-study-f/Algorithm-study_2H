from itertools import combinations

arr = ["abcdefghijklmnopqrstuvwxyz"]
ans = 0

for s in range(len(arr)): # 조합이 2개가 아니라 3개,4개 여러개가 될 수 있기 때문에 combination(arr,2)로 하면 안된다. 접근 자체가 틀렸었음
    for lst in combinations(arr,s+1):
        check = ''.join(lst)
        length = len(check)

        if length == len(set(check)):
            ans = max(ans,length)
print(ans)