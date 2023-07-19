def majorityElement(nums):
    return sorted(nums)[len(nums)//2]

nums = [6,5,5]

print(majorityElement(nums))