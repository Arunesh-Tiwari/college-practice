class Solution:
    
    def romanToInt(self, s: str) -> int:
        X = {'CM': 900,'CD': 400,'XC': 90,'XL': 40,'IX': 9,'IV': 4,'M': 1000,'D': 500,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        t = 0
        for i in X:
            count = s.count(i)
            t += count * X[i]
            s = s.replace(i, '')
        return t

