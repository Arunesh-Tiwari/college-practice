class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        summ = 0
        for i in range(len(nums)):
            summ = summ ^ nums[i]
        return summ