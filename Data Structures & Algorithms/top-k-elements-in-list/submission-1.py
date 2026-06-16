class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        d={}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return [key for key, _ in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]


        