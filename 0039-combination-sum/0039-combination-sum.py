import sys
sys.setrecursionlimit(15000)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return 0
        else:
            ans = []
            def dfs(ind, temp, total):
                if total == target:
                    ans.append(temp)
                    return
                if ind >= len(candidates) or total > target:
                    return
                
                dfs(ind+1, temp, total)
                dfs(ind, temp+[candidates[ind]], total+candidates[ind])
        dfs(0,[], 0)
        return ans