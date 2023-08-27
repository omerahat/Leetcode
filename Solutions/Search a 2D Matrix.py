def searchMatrix(matrix,target):

    leftMatrix = 0
    rightMatrix = len(matrix) - 1

    while leftMatrix <= rightMatrix:

        midMatrix = (leftMatrix + rightMatrix)//2

        if matrix[midMatrix][0] <= target <= matrix[midMatrix][-1]:

            leftNum = 0
            rightNum = len(matrix[midMatrix]) - 1 

            while leftNum <= rightNum:
                
                midNum = (rightNum + leftNum) // 2

                if matrix[midMatrix][midNum] == target:
                    return True
                
                else:
                    if target < matrix[midMatrix][midNum]:
                    
                        rightNum = midNum -1
                    
                    else:
                        
                        leftNum = midNum + 1
            
            return False

        else:

            if target < matrix[midMatrix-1][-1]:

                rightMatrix = midMatrix - 1

            else:

                leftMatrix = midMatrix + 1

    return False








matrix = [[1],[3],[5]]

target = 1
print(searchMatrix(matrix, target))