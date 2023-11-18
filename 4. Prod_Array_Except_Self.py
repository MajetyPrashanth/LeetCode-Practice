nums = [-1,1,0,-3,3]
final = [1]*len(nums)
prefix = 1
for i in range(len(nums)):
    final[i] = prefix
    prefix *= nums[i]
        
postfix = 1
for i in range(len(nums) -1, -1, -1):
    final[i] *= postfix
    postfix *= nums[i]
print(final)
