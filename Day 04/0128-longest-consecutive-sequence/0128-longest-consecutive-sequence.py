class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0
        for i in range(len(nums)):
            count = 0
            if nums[i]-1 not in numsSet:
                while nums[i]+count in numsSet:
                    count+=1
                    res = max(res,count)
        return res
