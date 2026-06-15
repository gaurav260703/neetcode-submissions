class Solution:
    def twoSum(self, arr: List[int], ans: int) -> List[int]:
        a={}
        for i in range(len(arr)):
            s=ans-arr[i]
            if s in a:
                return [a[s],i]
            a[arr[i]]=i
        return False
        