def majorityElement(nums):  # Solution 2 with Bayer Moore Algorithm
    result, count=0, 0

    for num in nums:
        if count==0:
            result=num
        if num!=result:
            count-=1
        else:
            count+=1
    return result


""" # Solution 2
def majorityElement(nums):
    return sorted(nums)[len(nums)//2]
"""

