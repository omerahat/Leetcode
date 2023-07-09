def removeDuplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k


nums = [1,1,1,1]
print(removeDuplicates(nums))
"""
def removeDuplicates(nums):

    for i in nums:
        while nums.count(i)>1:
            nums.remove(i)
    return len(nums)
"""