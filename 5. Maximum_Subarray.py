nums = [-2,1,-3,4,-1,2,1,-5,4]
current_sum = 0
subMax = nums[0]

for i in nums :
    if current_sum < 0 :
        current_sum = 0
    current_sum += i
    subMax = max(subMax, current_sum)
print(subMax)
