class MedianFinder:

    def __init__(self):
        self.mvb = []

    def addNum(self, num: int) -> None:
        self.mvb.append(num)
        

    def findMedian(self) -> float:
        self.mvb = sorted(self.mvb)
        mid = len(self.mvb)%2
        if mid==0:
            ans =  (self.mvb[len(self.mvb)//2-1] + self.mvb[len(self.mvb)//2])/2
            return round(ans,5)
        else:
            return self.mvb[len(self.mvb)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()