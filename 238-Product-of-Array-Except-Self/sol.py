class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        maxS=nums[0]
        for n in nums:
            if total<0: total=0
            total+=n
            maxS = max(total, maxS)
        return maxS
