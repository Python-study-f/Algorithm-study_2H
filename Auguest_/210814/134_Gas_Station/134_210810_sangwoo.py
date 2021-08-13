gas = list(map(int, input().split()))
cost = list(map(int, input().split()))
gas_sum = 0
cost_sum = 0
start = 0
temp = 0

for i in range(len(gas)):
     gas_sum += gas[i]
     cost_sum += cost[i]
     
if gas_sum < cost_sum: # 가스의 합이 소모값의 합보다 작으면 한바퀴를 돌 수 없음
    print("-1")
else:
    for i in range(len(gas)): 
        dif = gas[i] - cost[i]
        temp += dif # temp에 차이값을 저장
        if temp < 0:# 각각의 위치에서 소모값이 가스보다 크면 시작위치를 오른쪽으로 옮김
            start += 1
            temp = 0 # temp 초기화
    print(start)
