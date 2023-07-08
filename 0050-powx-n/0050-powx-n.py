class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        t = pow(x, n//2)
        if(n%2==1):
            return t*t*x
        return t*t