class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=1
        zero =0
        for i in range(len(nums)):
            if(nums[i]!=0) : num*= nums[i]
            else: zero+=1
        output = list()
        if zero==0:
            for i in range(len(nums)):
                output.append(num/nums[i])
        elif zero==1 : 
            for i in range(len(nums)):
                if(nums[i]==0) : output.append(num)
                else : output.append(0)
        else : output = [ 0 for _ in range(len(nums))]
        return output