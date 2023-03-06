class Solution:
    def twoSum(self,n,t) -> List[int]:
        L = len(n)
        d = [""]*L
        for i in range(L):
            if n[i] in d:
                return [i,d.index(n[i])]
            else:
                d[i]=t-n[i]
                
                
                
class Solution:
    def twoSum(self,n,t) -> List[int]:               
        d = {}
        for i, x in enumerate(n):
            if x in d:
                return [i,d[x]]
            elif x not in d:
                d[t-x]=i          
