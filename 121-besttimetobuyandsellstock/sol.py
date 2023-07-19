class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        minI = prices[0]
        for i in range(len(prices)):
                minI = min(minI, prices[i])   # 현재까지의 최소        
                best = max(best, prices[i]-minI)#현재 최대차
                # 이런 방법은 생각못했음.
                #10^5면 무조건 O(n) 이내로 풀어야 시간통과

        return best