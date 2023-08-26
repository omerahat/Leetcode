import heapq

def kClosest(points, k):
    minHeap=[]

    for x,y in points:
        distanceToOrigin = (x**2) + (y**2)
        minHeap.append([distanceToOrigin,x,y])

    heapq.heapify(minHeap)

    result = []

    while k>0:
        distance,x,y = heapq.heappop(minHeap)
        result.append([x,y])
        k -= 1

    return result
    

