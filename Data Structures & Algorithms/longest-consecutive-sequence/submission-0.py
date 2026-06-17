class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        ans=set(arr)
        ma=0
        for i in ans:
            count=0
            if i-1 not in ans:
                count+=1
                while i+1 in ans:
                    count+=1
                    i+=1
                ma=max(ma,count)
        return ma
        