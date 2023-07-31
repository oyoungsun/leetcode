class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # nums = sorted(nums)
        # prev = nums[0]
        # for i in range(1, len(nums)):
        #     if(prev==nums[i]) : return True
        #     else : prev = nums[i]
        # return False
        map = {}
        for i in range(0, len(nums)):
            if nums[i] in map : return True
            else : map[nums[i]] = i
        return False
        # if len(nums)==len(set(nums)):  이렇게 set()으로
        #  길이를 비교하면
        # 더 높은 성능으로 측정됨.
        #     return False 
        #     else:
        #     return True