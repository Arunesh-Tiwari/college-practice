class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        if len(nums)==1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            x = self.permute(nums)

            for j in x:
                j.append(n)
            ans.extend(x)
            nums.append(n)
        return ans