def findDuplicate(nums): # with floyd cycle dedection 
    slowPointer = 0
    fastPointer = 0
    
    while True:
        slowPointer = nums[slowPointer]
        fastPointer = nums[nums[fastPointer]]
        if slowPointer == fastPointer:
            break
    
    secondSlowPointer = 0

    while True:
        slowPointer = nums[slowPointer]
        secondSlowPointer = nums[secondSlowPointer]
        if slowPointer == secondSlowPointer:
            return slowPointer


"""
Time Complexity = O(n^2)

def findDuplicate(nums):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if i != j and nums[i] == nums[j]:
                return nums[i]


"""