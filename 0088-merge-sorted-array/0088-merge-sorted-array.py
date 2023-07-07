class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        for i in range(m):
            ans.append(nums1[i])
            
        for i in range(n):
            ans.append(nums2[i])
            
        for i in range(m+n):
            nums1[i] = ans[i]
            
        nums1.sort()