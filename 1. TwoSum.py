nums = [2,7,11,15]
target = 18
hashmap={}
for i, n in enumerate(nums):
    difference = target - n
    if difference in hashmap:
        print([hashmap[difference], i])
    hashmap[n] = i
