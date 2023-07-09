def twoSum(nums,target):
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and nums.index(complement) != i:
            complement_index = nums.index(complement)
            return [i,complement_index]


print(twoSum([3,2,4],6))

"""

def twoSum(nums,target):
    num_indices = {}
        
    for i, num in enumerate(nums):
        complement = target - num
            
        if complement in num_indices:
            return [num_indices[complement], i]
            
        num_indices[num] = i
        
    return []


"""


