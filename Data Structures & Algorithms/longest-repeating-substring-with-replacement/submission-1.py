class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxFreq=0
        hash=[0]*26
        count=0
        m=0
        for r in range(len(s)):
            a=ord(s[r])-ord('A')
            hash[a]+=1
            maxFreq=max(maxFreq,hash[a])
            count=(r-l+1)-maxFreq
            while (r - l + 1) - maxFreq > k:
                hash[ord(s[l]) - ord('A')] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
        