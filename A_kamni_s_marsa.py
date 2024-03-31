# ID 110842358 / 28 мар 2024, 22:45:57

n = int(input())
orders = list(map(int, input().split()))
m = int(input())
samples = list(map(int, input().split()))

orders.sort()
samples.sort()

count = 0
i, j = 0, 0

while i < n and j < m:
    if samples[j] >= orders[i]:  
        count += 1
        i += 1
    
    j += 1

print(count)
