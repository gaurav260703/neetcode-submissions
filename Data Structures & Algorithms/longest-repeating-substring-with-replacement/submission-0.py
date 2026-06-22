class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        n = len(s)
        for i in range(n):
            hash=[0]*26
            maxFreq=0
            for j in range(i, n):
                ad=ord(s[j])-ord('A')
                hash[ad]+=1
                maxFreq=max(maxFreq,hash[ad])
                changes = (j - i + 1) - maxFreq
                if changes <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break

        return maxLen
        