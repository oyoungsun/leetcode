class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curMin, curMax = 1, 1
        for i in nums : 
            if i==0 : 
                curMin, curMax = 1, 1
                continue
            temp = curMax*i
            curMax = max(i*curMax, i*curMin, i)
            curMin = min(temp, i*curMin, i)
            res = max(res, curMax, curMin)
        return res