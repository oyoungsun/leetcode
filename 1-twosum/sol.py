class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)): # 이 부분 주의, i+1부터 시작해야함.
                if(nums[i]+nums[j]==target) : return [i,j]