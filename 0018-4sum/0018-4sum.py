class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                low = j+1
                high = n-1

                while low<high:
                    if nums[i]+nums[j]+nums[low]+nums[high]==target:
                        ans.add((nums[i],nums[j],nums[low],nums[high]))
                        low += 1
                        high -= 1
                    elif nums[i]+nums[j]+nums[low]+nums[high]<target:
                        low += 1
                    else:
                        high -= 1
        return ans