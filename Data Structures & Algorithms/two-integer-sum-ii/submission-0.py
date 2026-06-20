class Solution:
    def twoSum(self, arr: List[int], suum: int) -> List[int]:
        i=0
        j=len(arr)-1
        ans=0
        while i<=j:
            ans=arr[i]+arr[j]
            if ans==suum:
                return [i+1,j+1]
            else:
                if ans>suum:
                    j-=1
                else:
                    i+=1
        return [-1,-1]
        