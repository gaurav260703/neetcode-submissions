class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in arr:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        f=list(d.keys())
        for v in range(k):
            ans.append(f[v])
        return ans

        