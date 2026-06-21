class Solution:
    def lengthOfLongestSubstring(self, a: str) -> int:
        lst=[]
        ans=0
        count=0
        for i in a:
            while i in lst:
                lst.pop(0)
                count-=1
            lst.append(i)
            count+=1
            ans=max(ans,count)
        return ans
        