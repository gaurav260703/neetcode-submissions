class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=sorted(tuple(s))
        x=sorted(t)
        for i in range(len(x)):
            if x[i]!=s[i]:
                return False
        return True
        