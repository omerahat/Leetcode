def leastBricks(wall):
    hashMap = {0:0} # key: index , value:gaps

    for row in wall:
        gapCount=0
        for brick in row[:-1]: 
            gapCount +=brick
            hashMap[gapCount] +=1

    return len(wall) - max(hashMap.values())




wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(leastBricks(wall))
