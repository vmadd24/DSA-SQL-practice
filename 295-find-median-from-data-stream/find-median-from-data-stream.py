import heapq

class MedianFinder:

    def __init__(self):

        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)
        self.isOdd = True
        

    def addNum(self, num: int) -> None:

        if self.isOdd:
            heapq.heappush(self.maxHeap, -num)
        
        else:
            heapq.heappush(self.minHeap, num)
        
        
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            x = -heapq.heappop(self.maxHeap)
            y = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -y)
            heapq.heappush(self.minHeap, x)

        self.isOdd = not self.isOdd        


    def findMedian(self) -> float:

        if not self.isOdd:
            return -self.maxHeap[0]
        
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()