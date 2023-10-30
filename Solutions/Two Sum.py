def twoSum(nums,target):
    HashMap = {}

    for index, number in enumerate(nums):
        complement = target - number
        if complement in HashMap:
            return [HashMap[complement], index]
        else:
            HashMap[number] = index




""" 
Solution 2
def twoSum(nums,target):
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and nums.index(complement) != i:
            complement_index = nums.index(complement)
            return [i,complement_index]

"""
