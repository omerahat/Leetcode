def searchInsert(nums,target):
    position=1
    if nums[position]<=target<=nums[position+1]:
        return position

    if nums[len(nums//2)]<target:
        position=len(nums//2)
        nums=nums[:len(nums)//2]
        searchInsert(nums,target)


    if nums[len(nums//2)]>target:
        position=len(nums//2)
        nums=nums[len(nums)//2:]
        searchInsert(nums,target)




