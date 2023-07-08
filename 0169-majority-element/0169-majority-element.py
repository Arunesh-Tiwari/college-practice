class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            l.append(i)
            b=max(l)
            key=list(d.keys())
            value=list(d.values())
            pos=value.index(b)
        return key[pos]