class Solution:
    def maxArea(self, arr: List[int]) -> int:
        ans=0
        i=0
        j=len(arr)-1
        while i<=j:
            if arr[i]<=arr[j]:
                s=arr[i]*(j-i)
            else:
                s=arr[j]*(j-i)
            ans=max(ans,s)
            if arr[i]<=arr[j]:
                i+=1
            else:
                j-=1
        return ans
    