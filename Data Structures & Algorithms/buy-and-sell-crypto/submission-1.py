class Solution:
    def maxProfit(self, a: List[int]) -> int:
        mp=float('inf')
        profit=0
        for i in a:
            if i<mp:
                mp=i
            else:
                profit=max(profit,i-mp)
        return profit
            