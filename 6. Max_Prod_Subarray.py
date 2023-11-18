nums = [2,3,-2,4]
result = max(nums)
current_max, current_min = 1, 1

for i in nums :
    t = current_max * i
    current_max = max(current_max * i, current_min * i, i)
    current_min = min(t, current_min * i, i)
    result = max(result, current_max)
print(result)
