def productExceptSelf(nums):

    if nums== [0] * len(nums):
        return nums

    resultList = [1] * len(nums)

    multiplication=1
    zeroCheck=False
    zeroCount=0
    for i in nums:
        if i !=0:
            multiplication*=i
        else:
            zeroCheck=True
            zeroCount+=1

    if zeroCount>1:
        return [0] * len(nums)
        
    for index,num in enumerate(resultList):
        if zeroCheck:
            if nums[index]==0:
                resultList[index]=multiplication
            else:
                resultList[index]=0
        else:
            resultList[index]=multiplication//nums[index]
        

    return resultList

