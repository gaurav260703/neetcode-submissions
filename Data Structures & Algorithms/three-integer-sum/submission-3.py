class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr=sorted(arr)
        uu=[]
        for i in range(len(arr)):
            if i>0 and arr[i]==arr[i-1]:
                continue
            j=i+1
            k=len(arr)-1
            while j<k:
                ans=arr[i]+arr[j]+arr[k]
                if ans==0:
                    uu.append([arr[i],arr[j],arr[k]])
                    j+=1
                    k-=1
                    while j<k and arr[j]==arr[j-1]:
                        j+=1
                    while j<k and arr[k]==arr[k+1]:
                        k-=1
                else:
                    if ans<0:
                        j+=1
                    elif ans>0:
                        k-=1                
        return uu
        