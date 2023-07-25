class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip(' ')
        s=list(s.split())
        ans=""
        for i in range(len(s)):
            ans = s[i]+" "+ans
        return ans.strip(' ')