import heapq

class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap,num * (-1))
        
        if self.smallHeap and self.largeHeap and (-1*self.smallHeap > self.largeHeap[0]):
            heapq.heappush(self.largeHeap, (-1*heapq.heappop(self.smallHeap)))
        
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            heapq.heappush(self.largeHeap, (-1*heapq.heappop(self.smallHeap)))  

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            heapq.heappush(self.smallHeap, (-1*heapq.heappop(self.largeHeap)))


    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return ((-1*self.smallHeap[0]) + self.largeHeap[0]) / 2
        elif len(self.smallHeap) > len(self.largeHeap):
            return -1*self.smallHeap[0]
        else:
            return self.largeHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()