def longestConsecutive(nums):

    numsSet=set(nums)

    longestStreak=0

    for num in numsSet:
        if num-1 not in numsSet:
            currentNum=num
            currentStreak=1

            while currentNum+1 in numsSet:
                currentNum+=1
                currentStreak+=1

            longestStreak=max(longestStreak,currentStreak)
    
    return longestStreak
