class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in arr:
            count=[0]*26

            for u in i:
                count[ord(u)-ord("a")]+=1
            a[tuple(count)].append(i)
        return list(a.values())
        