class Solution:
    def trap(self, a: List[int]) -> int:
        l=0
        r=len(a)-1
        lfmax=0
        rtmax=a[r]
        total=0
        while l<r:
            if a[l]<a[r]:
                if lfmax>a[l]:
                    total+=lfmax-a[l]
                else:
                    lfmax=a[l]
                l+=1
            else:
                if rtmax>a[r]:
                    total+=rtmax-a[r]
                else:
                    rtmax=a[r]
                r-=1
        return total