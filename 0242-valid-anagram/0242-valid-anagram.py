class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        n = len(s)
        t = list(t)
        count = 0
        if len(s)==len(t):
            for i in range(len(t)):
                if t[i] in s:
                    count+=1
                    x = s.index(t[i])
                    del s[x]
                 
        if count == n:
            return True
        else:
            return False
            
